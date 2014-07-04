import numpy as np
import string

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
                    other = np.random.choice([vert for vert in self.least_conn() if vert != v and self.get_edge(v, vert) is None])
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

class Vertex(object):
    def __init__(self, label = ''):
        self.label = label
        self.marked = False

    def __repr__(self):
        return 'Vertex({0})'.format(repr(self.label))

    __str__ = __repr__

    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1,e2))

    def __repr__(self):
        return 'Edge({0}, {1})'.format(repr(self[0]), repr(self[1]))

    __str__ = __repr__
