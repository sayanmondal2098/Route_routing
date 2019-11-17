#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# In[26]:



import numpy as np
import networkx as nx

import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


G = nx.Graph()
G.nodes(), G.edges()


# CREATE THE 12 NODES OF THE GRAPH

# In[20]:



for i in range(1,13):
    G.add_node(i)
G.nodes()


# In[21]:


print ('number of nodes in the graph :',G.number_of_nodes())


# In[16]:


# ADD EDGES


# In[22]:


G.add_edges_from([(1,2), (1,4),(2,3),(2,5),(3,6),(4,5),(4,7),(5,6),(5,8),(6,9),(7,8),(7,10),(8,9),(8,11),(9,12),(10,11),(11,12)]) 


# In[23]:


print(G.nodes())
print('number of edges in the graph:', G.number_of_edges())
print('edges in the graph:', G.edges())
print('degree counts per node:', G.degree())


# In[24]:


G.neighbors(1) # neighbor of node 1


# In[27]:


nx.draw_networkx(G, with_labels=True)
plt.show()

print(nx.shortest_path(G, source=1, target=11))

# In[ ]:




