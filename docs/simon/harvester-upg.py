from diagrams import Diagram, Edge
from diagrams.aws.compute import ECS

graph_attr = {
    "fontsize": "36",
}

edge_attr = {
    "fontsize": "45",
}

node_attr = {
    "fontsize": "16",
}

with Diagram("Harvester Upgrade Paths", show=False, outformat="png", graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
    rel_1_0_0 = ECS("1.0.0")
    rel_1_0_1 = ECS("1.0.1")
    rel_1_0_2 = ECS("1.0.2")
    rel_1_0_3 = ECS("1.0.3")
    rel_1_1_0 = ECS("1.1.0")
    rel_1_1_1 = ECS("1.1.1")
    rel_1_1_2 = ECS("1.1.2")
    rel_1_2_0 = ECS("1.2.0")
    rel_1_2_1 = ECS("1.2.1")

    rel_1_0_0 >> rel_1_0_1
    rel_1_0_1 >> rel_1_0_2
    rel_1_0_2 >> rel_1_0_3
    rel_1_0_3 >> rel_1_1_0
    rel_1_0_3 >> rel_1_1_1
    rel_1_1_0 >> rel_1_1_1
    rel_1_1_0 >> rel_1_1_2
    rel_1_1_1 >> rel_1_1_2
    rel_1_1_2 >> Edge(label="Not recommended",
                      color="red", style="dotted") >> rel_1_2_0
    rel_1_1_2 >> rel_1_2_1
    rel_1_2_0 >> rel_1_2_1
