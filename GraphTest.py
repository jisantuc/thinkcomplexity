from Graph import *
from GraphWorld import *
import string
from pprint import pprint

labels = string.ascii_lowercase
n_vertices = 20
vs = [Vertex(v) for v in labels[:n_vertices]]

g = Graph(vs)

g.add_regular_edges(2)
layout = CircleLayout(g)


print g.is_connected()
gw = GraphWorld()
gw.show_graph(g, layout)
gw.mainloop()
