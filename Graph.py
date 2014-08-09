import numpy as np
import string
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil
from pprint import pprint

class Graph(dict):    
    def __init__(self, vs = [], es = []):
        """create a new graph. (vs) is a list of vertices, (es) is a list of edges"""
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self,v):
        """add (v) to the graph"""
        self[v] = {}

    def add_edge(self, e):
        """add (e) to the graph by adding an entry in both directions.
        If there is already an edge connecting these Vertices, the new
        edge replaces it"""
        v,w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        """checks whether an edge exists between v1 and v2. If no edge exists, returns None"""
        try:
            return self[v1][v2]
        except(KeyError):
            return None

    def remove_edge(self,e):
        """removes all references to e"""
        self[e[0]].pop(e[1])
        self[e[1]].pop(e[0])

    def vertices(self):
        """returns list of vertices in graph"""
        return self.keys()

    def edges(self):
        """returns a list of edges in graph"""
        out = []
        for i in self.keys():
            for k in self.keys():
                out.append(self.get_edge(i,k))
        return [o for o in out if o is not None]

    def out_vertices(self, vertex):
        """returns list of adjacent vertices"""
        return self[vertex].keys()

    def out_edges(self, vertex):
        """returns list of all edges connected to vertex"""
        return [self[vertex][k] for k in self[vertex].keys()]

    def add_all_edges(self):
        for u in self.vertices():
            for v in [vert for vert in self.vertices() if vert != u]:
                if self.get_edge(u,v) is None:
                    self.add_edge((u,v))

    def degree(self):
        """returns degree of graph"""
        return len(self.vertices())

    def least_conn(self):
        """finds the vertex with the fewest connections"""
        minimum = min([len(self.out_edges(v)) for v in self.vertices()])
        return [v for v in self.vertices() if len(self.out_edges(v)) == minimum]
    
    def add_regular_edges(self, order):
        """starts with an edgeless graph and adds order edges to every vertex
           fails if regular graph can't be drawn or if graph is not edgeless"""        
        if len(self.edges()) != 0:
            print 'Graph is not edgeless'
        elif self.degree() >= order + 1 and (self.degree() * order) % 2 == 0:
            for v in self.vertices():
                while(len(self.out_edges(v)) < order):
                    try:
                        other = np.random.choice([vert for vert in self.least_conn() if vert != v and self.get_edge(v, vert) is None])
                    except(ValueError):
                        other = np.random.choice([vert for vert in self.vertices() if vert != v and len(self.out_edges(vert)) <= order])
                    self.add_edge((v,other))
        else:
            print 'No {0}-regular graph exists for degree {1}'.format(order, self.degree())

    def is_connected(self):
        start = np.random.choice(self.vertices())
        queue = [start]
        conn = []
        while(len(queue) > 0):
            popped = queue.pop()
            popped.mark()
            conn = conn + [popped]
            queue = queue + [v for v in self.out_vertices(popped) if v not in queue and not v.marked]
        if len(conn) == len(self.vertices()):
            for v in self.vertices():
                v.unmark()
            return True
        elif len(conn) > len(self.vertices()):
            print "This should never have happened something is terribly wrong."
        else:
            for v in self.vertices():
                v.unmark()         
            return False

class RandomGraph(Graph):
    def add_random_edges(self,p):
        """adds edges to an edgeless graph between any two vertices with probability p"""
        if len(self.edges()) == 0:
            start = self.vertices()
            while(len(start) > 1):
                v = start.pop(0)
                for u in start:
                    if np.random.uniform() < p:
                        self.add_edge((v, u))
        else:
            print "Graph was not edgeless."

class SmallWorldGraph(Graph):
    def __init__(self, vs = [], degree = 2):
        for v in vs:
            self.add_vertex(v)
        self.add_regular_edges(degree)
        self.degree = degree

    def rewire(self, p):
        edges_to_add = []        
        for e in self.edges():
            try:
                if np.random.uniform() < p and e not in edges_to_add:
                    source = e[0]
                    term = e[1]
                    new_term = np.random.choice([v for v in self.vertices() if v != term and v != source])
                    edges_to_add.append(Edge(source, new_term))
                    print 'rewiring edge ({0},{1})...'.format(source,term)
                    self.remove_edge(e)
                else:
                    pass #showing explicitly that values below p result in doing nothing
            except(KeyError):
                pass
        for e in edges_to_add:
            self.add_edge(e)

    def connection_perc(self, v):
        return len(self.out_edges(v))/float(len(self.vertices()))

    def clustering_coefficient(self, normalized = False):
        c_v = np.array([self.connection_perc(v) for v in self.vertices()])
        
        if normalized:
            comp_graph = SmallWorldGraph(vs = self.vertices(), degree = self.degree)
            c_0 = comp_graph.clustering_coefficient()
            print 'c_0 = {0}'.format(c_0)
            return c_v.mean()/comp_graph.clustering_coefficient()
        else:        
            return c_v.mean()

    def new_queue(self, run):
        opts = {vert for vert in self.vertices() if vert.distance == run}
        queue = []
        while opts:
            try:            
                v = opts.pop()
                queue += [vert for vert in self.out_vertices(v) if vert.distance > run and vert not in queue]
                #pprint(queue)
            except IndexError:
                pass
        return queue


    def Dijkstra(self):
        
        if self.is_connected():
            v = self.least_conn().pop()
            v.distance = 0
            d = {vert: vert.distance for vert in self.vertices() if vert.distance != float('inf')}

            queue = self.out_vertices(v)
            run = 1

            while len(d) < len(self.vertices()) - 1:
                while queue:
                    q = queue.pop()
                    q.set_distance(run)

                d = {vert:vert.distance for vert in self.vertices() if vert.distance != float('inf')}
                queue = self.new_queue(run)

                run = run + 1

            for vert in self.vertices():
                vert.distance = float('inf')

            return sum(d.values()) / (len(d.values()) - 1.)

        else:
            print 'Graph is not connected.'
            return None

    def sw_plot(self):
        x = np.array([p for p in np.linspace(0.001,0.3,300)])
        y = list()
        
        for p in x:
            base = self
            base.rewire(p)
            y = y + [base.clustering_coefficient(normalized = True)]
        y = np.array(y)
        y = y/y.max()
            
        plotted = plt.plot(x,y, 'ro')
        plt.title('Clustering coefficient for varying values of p')
        plt.xlabel('Probability of rewire')
        plt.ylabel('Clustering Coefficient')
        plt.axis([0.,0.3,0.,ceil(y.max())])
        
        

class Vertex(object):
    def __init__(self, label = ''):
        self.label = label
        self.marked = False
        self.distance = float('inf')

    def __repr__(self):
        return 'Vertex({0})'.format(repr(self.label))

    __str__ = __repr__

    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False

    def set_distance(self, d):
        self.distance = d

    def clear_distance(self):
        self.distance = float('inf')

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1,e2))

    def __repr__(self):
        return 'Edge({0}, {1})'.format(repr(self[0]), repr(self[1]))

    __str__ = __repr__

class DoublyLinkedList(Graph):
    def __init__(self, nodes = []):
        self.stop = DoublyLinkedNode(label = 'stop')
        nodes = [self.stop] + nodes

        for n in nodes:
            self.add_vertex(n)

        for i, n in enumerate(nodes):
            if i != len(nodes) - 1:
                n.foll = nodes[i+1]
                n.prec = nodes[i-1]
            else:
                n.foll = self.stop
                n.prec = nodes[i-1]

        for n in nodes:
            self.add_edge((n,n.foll))

    def append(self, node):
        self.remove_edge((self.stop, self.stop.prec))
        self.add_vertex(node)
        self.add_edge((self.stop.prec, node))
        self.add_edge((node, self.stop))
        self.stop.prec = node

    def pop(self):
        popped = self.stop.foll
        for e in self.out_edges(popped):
            self.remove_edge(e)
        self.add_edge((self.stop, popped.foll))
        self.stop.foll = popped.foll
        return popped
        


class DoublyLinkedNode(Vertex):
    def __init__(self, label = '', prec = None, foll = None):
        self.label = label
        self.prec = prec
        self.foll = foll
