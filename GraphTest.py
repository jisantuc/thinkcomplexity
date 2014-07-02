#from Graph import *
from GraphWorld import *
import string
from pprint import pprint
from RandomGraph import RandomGraph

labels = string.ascii_lowercase
n_vertices = 10
vs = [Vertex(v) for v in labels[:n_vertices]]

g = RandomGraph(vs)

g.add_random_edges(0.2)
layout = CircleLayout(g)

gw = GraphWorld()
gw.show_graph(g, layout)
gw.mainloop()
