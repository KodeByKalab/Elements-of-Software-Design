#  File: Graph.py

#  Description: A graph implementation with operations for transversal and deletion of edges and vertices



import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []
        self.directed = True

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.directed = True
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.directed = False
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        # create a queue
        bfs_stack = Queue()

        (self.Vertices[v]).visited = True  # mark visited
        print(self.Vertices[v])
        bfs_stack.enqueue(v)  # enqueue

        while not bfs_stack.is_empty():
            # obtain vertex at the front and adjacent unvisited vertex
            front_vert = bfs_stack.dequeue()
            adj_vert = self.get_adj_unvisited_vertex(front_vert)
            while adj_vert != -1:
                (self.Vertices[adj_vert]).visited = True
                print(self.Vertices[adj_vert])
                bfs_stack.enqueue(adj_vert)
                adj_vert = self.get_adj_unvisited_vertex(front_vert)

        # queue is empty reset the flags
        numVert = len(self.Vertices)
        for i in range(numVert):
            (self.Vertices[i]).visited = False

        ### optional functions

    def printMat(self):
        for row in self.adjMat:
            s = ""
            for c in row:
                s += str(c)
                s += " "
            print(s[:-1])
        return

    def delete_edge(self, fromVertexLabel, toVertexLabel):
        self.adjMat[fromVertexLabel][toVertexLabel] = 0
        self.adjMat[toVertexLabel][fromVertexLabel] = 0

        return

    def get_vertices(self):
        vertices_list_copy = []  # obtain a copy of vertices
        for v in self.Vertices:
            vertices_list_copy.append(v)
        return vertices_list_copy

    def delete_vertex(self, vertexLabel):
        labels = [vertex.label for vertex in self.Vertices]
        idx = labels.index(vertexLabel)
        self.Vertices.pop(idx)
        for row in self.adjMat:
            row.pop(idx)
        self.adjMat.pop(idx)

        return


def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # do the depth first search
    print("Depth First Search")
    cities.dfs(start_index)
    print()

    # BFS test case
    print("Breadth First Search")
    cities.bfs(start_index)
    print()

    # edge deletion test
    edges = sys.stdin.readline().strip().split()
    fromIdx = cities.get_index(edges[0])
    toIdx = cities.get_index(edges[1])
    print("Deletion of an edge")
    #cities.printMat()
    print()
    print("Adjacency Matrix")
    cities.delete_edge(fromIdx, toIdx)
    # cities.delete_edge(10, 8)
    cities.printMat()
    print()

    # vertex deletion test
    print("Deletion of a vertex")
    print()
    deleteMe = sys.stdin.readline().strip()
    cities.delete_vertex(deleteMe)
    print("List of Vertices")
    for city in cities.get_vertices():
        print(city)
    print()
    print("Adjacency Matrix")
    cities.printMat()
    print()


if __name__ == "__main__":
    main()
