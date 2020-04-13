from data_structure import Edge
from typing import TypeVar, Generic, List
from search import bfs, dfs, node_path


V = TypeVar("V")

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []):
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        return len(self._edges)

    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge: Edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int):
        edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, fr: V, to: V):
        self.add_edge_by_indices(
            self._vertices.index(fr),
            self._vertices.index(to)
        )

    def vertex_at(self, index: int):
        return self._vertices[index]

    def index_of(self, vertex: V):
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index: int):
        return list(map(self.vertex_at, [edge.v for edge in self._edges[index]]))

    def neighbors_for_vertex(self, vertex: V):
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index: int):
        return self._edges[index]

    def edges_for_vertex(self, vertex: V):
        return self.edges_for_index(self.index_of(vertex))

    def search_bfs(self, u: V, v: V):
        node = bfs(u, lambda vertex: True if vertex == v else False, self.neighbors_for_vertex)
        return node_path(node)

    def search_dfs(self, u: V, v: V):
        node = dfs(u, lambda vertex: True if vertex == v else False, self.neighbors_for_vertex)
        return node_path(node)

    def __str__(self):
        string = ""
        for i in range(self.vertex_count):
            string += "{} -> {}\n".format(self.vertex_at(i), self.neighbors_for_index(i))
        return string 


    
if __name__ == "__main__":
    graph: Graph[str] = Graph([
        "São Paulo",
        "Rio de Janeiro",
        "Porto Alegre",
        "Brasilia",
    ])
    graph.add_edge_by_vertices("Porto Alegre", "São Paulo")
    graph.add_edge_by_vertices("São Paulo", "Rio de Janeiro")
    graph.add_edge_by_vertices("Rio de Janeiro", "Brasilia")
    print(graph)

    print(graph.search_bfs("Porto Alegre", "Brasilia"))
    