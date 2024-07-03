import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def creaGrafo(self,y,l):
        print("creo grafo")
        self.idMap = {}
        self.grafo = nx.DiGraph()
        self.nodi = l
        for n in l:
            self.idMap[n.id] = n
        self.edges = DAO.getArco(y,self.idMap)
        self.grafo.add_nodes_from(self.nodi)
        self.grafo.add_edges_from(self.edges)

    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self.grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited
    def analisi(self,s ):
        return self.grafo.successors(s),self.grafo.predecessors(s)

    def stampa(self):
        return f"nodi: {len(self.grafo.nodes)}, archi: {len(self.grafo.edges)}"
