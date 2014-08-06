from Graph import *
from GraphWorld import *
import string
from pprint import pprint

labels = string.ascii_lowercase
n_vertices = 1000
vs = [Vertex(v) for v in labels[:n_vertices]]

for n in range(1,11):
    sw = SmallWorldGraph(vs = vs, degree = n)
    sw.graph_clustering_coefficient()

#g = Graph(vs)

#g.add_regular_edges(2)
"""layout = CircleLayout(sw)


#print g.is_connected()
gw = GraphWorld()
#gw.show_graph(dll, layout)

gw.show_graph(sw, layout)
gw.mainloop()

#dll.append(DoublyLinkedNode('lolz'))"""
