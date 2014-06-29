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
        self[e[0]][e[1]] = {}
        self[e[1]][e[0]] = {}

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

#number 7: out_vertices

class Vertex(object):
    def __init__(self, label = ''):
        self.label = label

    def __repr__(self):
        return 'Vertex({0})'.format(repr(self.label))

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1,e2))

    def __repr__(self):
        return 'Edge({0}, {1})'.format(repr(self[0]), repr(self[1]))

    __str__ = __repr__
