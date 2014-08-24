from Graph import Graph
import numpy as np

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
