from Graph import *
from GraphWorld import *
import string
from pprint import pprint
import numpy as np

#labels = string.ascii_lowercase
n_vertices = 50
labels = range(n_vertices)
vs = [Vertex(str(v)) for v in labels]

sw = SmallWorldGraph(vs = vs, degree = 5)

sw.sw_plot(0.1)

"""#g = Graph(vs)

#g.add_regular_edges(2)
layout = CircleLayout(sw)


#print g.is_connected()
gw = GraphWorld()
#gw.show_graph(dll, layout)

gw.show_graph(sw, layout)
gw.mainloop()

#dll.append(DoublyLinkedNode('lolz'))"""
