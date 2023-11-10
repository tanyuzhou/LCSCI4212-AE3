<template>
    <div class="svg-container">
        <svg class="graph"></svg>
    </div>
</template>

<script>
import * as d3 from 'd3'

export default {
    name: 'HomeView',
    data() {
        return {
            adjacencyMatrix: [
                [0, 12, 0, 0, 0, 16, 14],
                [12, 0, 10, 0, 0, 7, 0],
                [0, 10, 0, 3, 5, 6, 0],
                [0, 0, 3, 0, 4, 0, 0],
                [0, 0, 5, 4, 0, 2, 8],
                [16, 7, 6, 0, 2, 0, 9],
                [14, 0, 0, 0, 8, 9, 0]
            ], 
            nodes: [], 
            firstTick: true, 
        }
    },
    mounted() {
        this.nodes = Array.from({ length: this.adjacencyMatrix.length }, (_, i) => {
            let name = String.fromCharCode(65 + i);
            if (i >= 26) {
                name = String.fromCharCode(65 + Math.floor(i / 26) - 1) + String.fromCharCode(65 + i % 26);
            }
            return { name: name, fx: null, fy: null };
        });

        // Create an SVG container
        const svg = d3.select("svg");

        // Define the dimensions and margins for the graph
        // 获取svg实际的宽高
        const width = svg.node().getBoundingClientRect().width;
        const height = svg.node().getBoundingClientRect().height;
        const margin = { top: 50, right: 50, bottom: 50, left: 50 };
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        // Manually set positions
        this.nodes.forEach((node, i) => {
            node.fx = innerWidth / 2 + (Math.cos(i * 2 * Math.PI / this.nodes.length) * -1) * innerWidth / 3;
            node.fy = innerHeight / 2 + (Math.sin(i * 2 * Math.PI / this.nodes.length) * -1) * innerHeight / 3;
            console.log(Math.cos(i * 2 * Math.PI / this.nodes.length), Math.sin(i * 2 * Math.PI / this.nodes.length))
        });

        // Create a graph layout
        const simulation = d3
            .forceSimulation(this.nodes)
            .nodes(this.nodes)
            .force(
                "link",
                d3
                    .forceLink()
                    .id((d) => d.index)
                    .links(
                        this.adjacencyMatrix.reduce((links, row, sourceIndex) => {
                            row.forEach((weight, targetIndex) => {
                                if (weight > 0 && sourceIndex < targetIndex) {
                                    links.push({ source: sourceIndex, target: targetIndex, weight });
                                }
                            });
                            return links;
                        }, [])
                    )
                    .distance(200) // Increase this value
            )
            .force("charge", d3.forceManyBody().strength(-300))
            .force("center", d3.forceCenter(innerWidth / 2, innerHeight / 2))
            .force("collide", d3.forceCollide().radius(30));

        // Create links
        const links = svg
            .selectAll("line")
            .data(simulation.force("link").links())
            .enter()
            .append("line")
            .style("stroke", "black");

        // Create nodes
        const nodesSelection = svg
            .selectAll("circle")
            .data(simulation.nodes())
            .enter()
            .append("circle")
            .attr("r", 20)
            .style("fill", "lightblue")
            .call(this.drag(simulation)); // Make the nodes draggable

        // Add labels to nodes
        const labels = svg
            .selectAll(null)
            .data(simulation.nodes())
            .enter()
            .append("text")
            .text((d) => d.name)
            .style("text-anchor", "middle")
            .style("alignment-baseline", "middle");

        // Add weights to links
        const linkWeights = svg
            .selectAll(null)
            .data(simulation.force("link").links())
            .enter()
            .append("text")
            .text((d) => d.weight)
            .style("stroke", "#09e")
            .style("stroke-width", "1px")
            .style("fill", "#fff")
            .style("font-size", "27px")
            .style("font-weight", "bold")
            .style("text-anchor", "middle")
            .style("alignment-baseline", "middle")

        // Start the simulation
        simulation.on("tick", () => {
            // console.log("tick")
            if(this.firstTick) {
                this.firstTick = false;
                this.nodes.forEach((node, i) => {
                    node.fx = null;
                    node.fy = null;
                });
            }
            nodesSelection
                .attr("cx", (d) => d.x)
                .attr("cy", (d) => d.y);
            labels
                .attr("x", (d) => d.x)
                .attr("y", (d) => d.y);
            links
                .attr("x1", (d) => d.source.x)
                .attr("y1", (d) => d.source.y)
                .attr("x2", (d) => d.target.x)
                .attr("y2", (d) => d.target.y);
            linkWeights
                .attr("x", (d) => (d.source.x + d.target.x) / 2)
                .attr("y", (d) => (d.source.y + d.target.y) / 2);
        });

        console.log(simulation)
    },
    methods: {
        drag(simulation) {
            function dragstarted(event) {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                event.subject.fx = event.subject.x;
                event.subject.fy = event.subject.y;
            }

            function dragged(event) {
                event.subject.fx = event.x;
                event.subject.fy = event.y;
            }

            function dragended(event) {
                if (!event.active) simulation.alphaTarget(0);
                event.subject.fx = null;
                event.subject.fy = null;
            }

            return d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended);
        }, 
    }
};
</script>

<style scoped>
.svg-container {
    width: 100%;
    height: 100vh;
}

.graph {
    width: 100%;
    height: 100%;
}

.link {
    stroke: #999;
    stroke-opacity: 0.6;
}

.node {
    fill: #ccc;
    stroke: #fff;
    stroke-width: 1.5px;
}

:global(svg > text) {
    user-select: none;
    -webkit-user-select: none;
    pointer-events: none;
}
</style>
