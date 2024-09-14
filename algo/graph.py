
class Graph:

    def __init__(self, N):
        self.size = N 
        self.nodes = [ [] for _ in range(N) ]
        self.visited = [False]*N

    def add_edge(self, first_node, second_node):
        if first_node < self.size and second_node < self.size:
            self.nodes[first_node].append(second_node)

    def add_double_edge(self, first_node, second_node):
        if first_node < self.size and second_node < self.size:
            self.nodes[first_node].append(second_node)
            self.nodes[second_node].append(first_node)

    def add_edges(self, edges_list):
        for begin, end in edges_list:
            self.add_edge(begin, end)

    def inner_dfs(self, node, action):
        action(node)
        for end in self.nodes[node]:
            if self.visited[end] == False:
                self.visited[end] = True
                self.inner_dfs(end, action)

    def dfs(self, start, action = lambda n: print(n) ):
        for i in range(self.size): self.visited[i] = False

        self.inner_dfs(start, action)

    def bfs(self, start, action = lambda n: print(n) ):
        for i in range(self.size): self.visited[i] = False
        
        q = [start]

        while not len(q) == 0:
            node = q.pop(0)
            if self.visited[node]: continue

            self.visited[node] = True
            action(node)

            for end in self.nodes[node]:
                if self.visited[end] == False:
                    q.append(end)

    def dijkstra();
    def kruskal():
    def prime():
    def flow():
        def topology_sort():
    def 

if __name__ == "__main__":
    G = Graph(10)
    G.add_edges([[0,1],[1,2],[2,3],[3,4],[4,5],[0,6],[6,7],[6,8],[3,9]])

    
        
        
