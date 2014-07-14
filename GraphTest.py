from Graph import *
from GraphWorld import *
import string
from pprint import pprint

labels = string.ascii_lowercase
n_vertices = 5
vs = [DoublyLinkedNode(v) for v in labels[:n_vertices]]

dll = DoublyLinkedList(vs)
dll.append(DoublyLinkedNode(label = 'lolz'))
dll.append(DoublyLinkedNode(label = 'haha'))

#g = Graph(vs)

#g.add_regular_edges(2)
layout = CircleLayout(dll)


#print g.is_connected()
gw = GraphWorld()
#gw.show_graph(dll, layout)

gw.show_graph(dll, layout)
gw.mainloop()

#dll.append(DoublyLinkedNode('lolz'))
