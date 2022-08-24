# This is a UNDIRECTED, UNWEIGHTED graph implementation.
class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjList = {}
        """
            adj list will look like: {
              0: [1,2],
              1: [0],
              ...
            }
        """

    def add_vertex(self, node):
        if node in self.adjList:
            return
        self.adjList[node] = []
        self.numberOfNodes += 1

    def add_edge(self, node1, node2):
        if node1 not in self.adjList or node2 not in self.adjList:
            return
        if node2 not in self.adjList[node1]:
            self.adjList[node1].append(node2)
        if node1 not in self.adjList[node2]:
            self.adjList[node2].append(node1)

    def show_connections(self):
        for key, nodes in self.adjList.items():
            print(key, "-->", ", ".join(nodes))


# -----------------
myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')
myGraph.show_connections()
