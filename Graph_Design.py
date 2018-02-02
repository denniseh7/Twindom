#Dennis Hsu
#Barebones Graph Class that was Augmented
#February 1, 2018
#Language: Python

#Graph Class
#Functions include: Add Vertex, Get Vertex, Add Edge, Remove Edge, Get Neighbors, Check if 2 Vertices are Adjacent
class Graph:

    #initiate vertices with list of neighbors
    def __init__(self):
        self.vertices={}

    #add new vertex with empty set of neighbors
    def AddVertex(self,new_vert):
        self.vertices[new_vert]=set()

    def GetVertices(self):
        return self.vertices

    #no duplicate edges (e.g. only 1 edge between 2 vertices possible); therefore no duplicate neighbors
    def AddEdge(self,v1,v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    #remove edge if necessary
    def RemoveEdge(self,v1,v2):
        self.vertices[v1].discard(v2)
        self.vertices[v2].discard(v1)

    #lookup of neighbors
    def Neighbors(self,v1):
        return self.vertices[v1]

    #check to see if two vertices are adjacent and thus incident to an edge
    def Adjacent(self,v1,v2):
        if v2 in self.vertices[v1] and v1 in self.vertices[v2]:
            return True
        return False

#Testing the graph
my_graph=Graph()

#adding vertexes to graph
my_graph.AddVertex("a")
my_graph.AddVertex("b")
my_graph.AddVertex("c")

#adding edges to graph
my_graph.AddEdge("a","b")
#test duplicates
my_graph.AddEdge("a","c")
my_graph.AddEdge("a","c")

print(my_graph.GetVertices()) #prints dictionary of vertices with set of neighbors/edges
print(my_graph.Neighbors("a")) #returns vertex a's neighbors

#test if vertices are adjacent (thus incident to the same edge)
print(my_graph.Adjacent("c","a")) #should return true
print(my_graph.Adjacent("b","c")) #should return false









