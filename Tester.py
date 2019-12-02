import ProbabilityFunction
import dijkstra1


matrix = []

edgeslist = ProbabilityFunction.matrixEdges(matrix,ProbabilityFunction.n)

# print(edgeslist)


graph = dijkstra1.Graph(ProbabilityFunction.n*ProbabilityFunction.n)

print("The Graph is (Src , Destination , weight)")
for i in edgeslist:
    # graph.add_edge(i)
    u = i["pt1"]
    v = i["pt2"]
    w = i["weight"]
    print(u,v,w)
    graph.add_edge(u,v,w)

print("The Graph is ")
# graph.show_graph()
# graph.dijkstra(1)
graph.show_path(0, 4)    