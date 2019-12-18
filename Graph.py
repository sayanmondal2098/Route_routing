import ProbabilityFunction
import dijkstra


src = int(input("Enter node of packet Src : "))
dest = int(input("Enter node of packet destination : "))

matrix = []

edgeslist = ProbabilityFunction.matrixEdges(matrix,ProbabilityFunction.n)

# print(edgeslist)


graph = dijkstra.Graph(ProbabilityFunction.n*ProbabilityFunction.n)
# graph = Graph()
print("The Graph is (Src , Destination , weight)")
for i in edgeslist:
    # graph.add_edge(i)
    u = i["pt1"]
    v = i["pt2"]
    w = i["weight"]
    print(u,v,w)
    graph.addEdge(u,v,w)



print ("Shortest Path between %d and %d is " %(src, dest)), 
l = graph.findShortestPath(src, dest)   

print ("\nShortest Distance between %d and %d is %d " %(src, dest, l)), 
