import networkx as nx
from networkx.algorithms.flow import maximum_flow

import matplotlib.pyplot as plt 


G = nx.DiGraph()
# G.add_edges_from([(1, 2, {'capacity': 1, 'weight': 1}),
#                    (1, 4, {'capacity': 1, 'weight': 1}),
#                    (2, 3, {'capacity': 1, 'weight': 1}),
#                    (2, 5, {'capacity': 1, 'weight': 1}),
#                    (3, 1, {'capacity': 1, 'weight': 1}),
#                    (4, 5, {'capacity': 1, 'weight': 1}),
#                    (4, 7, {'capacity': 1, 'weight': 1}),
#                    (5, 1, {'capacity': 1, 'weight': 1}),
#                    (5, 8, {'capacity': 1, 'weight': 1}),
#                    (1, 9, {'capacity': 1, 'weight': 1}),
#                    (7, 8, {'capacity': 1, 'weight': 1}),
#                    (7, 10, {'capacity': 1, 'weight': 1}),
#                    (8, 9, {'capacity': 1, 'weight': 1}),
#                    (8, 11, {'capacity': 1, 'weight': 1}),
#                    (9, 12, {'capacity': 1, 'weight': 1}),
#                    (10, 11, {'capacity': 1, 'weight': 1}),
#                    (11, 12, {'capacity': 1, 'weight': 1}),
                   
#                    ])

G.add_edges_from([(1,2), (1,4),(2,3),(2,5),(3,6),(4,5),(4,7),(5,6),(5,8),(6,9),(7,8),(7,10),(8,9),(8,11),(9,12),(10,11),(11,12)]) 

flowDict = nx.min_cost_flow(G)
print(flowDict)
# maxFlow = maximum_flow(G, 1, 7)[1]
# nx.cost_of_flow(G, maxFlow) >= mincost

# mincostFlowValue = (sum((mincostFlow[u][7] for u in G.predecessors(7)))
#                      - sum((mincostFlow[7][v] for v in G.successors(7))))
# mincostFlowValue == nx.maximum_flow_value(G, 1, 7)

nx.draw_networkx(G)
# nx.draw_networkx(mincost)

plt.show()


nx.draw_networkx(flowDict)
# nx.draw_networkx(mincost)

plt.show()