from Graph import *
from GraphWorld import *
import string
from pprint import pprint

labels = string.ascii_lowercase
n_vertices = 26
vs = [Vertex(v) for v in labels[:n_vertices]]

sw = SmallWorldGraph(vs = vs, degree = 5)
sw.rewire(0.02)

print sw.Dijkstra()

#g = Graph(vs)

#g.add_regular_edges(2)
"""layout = CircleLayout(sw)


#print g.is_connected()
gw = GraphWorld()
#gw.show_graph(dll, layout)

gw.show_graph(sw, layout)
gw.mainloop()

#dll.append(DoublyLinkedNode('lolz'))"""
