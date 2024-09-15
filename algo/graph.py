from queue import PriorityQueue

class Graph:

    def __init__(self, N):
        self.size = N 
        self.E = [ [] for _ in range(N) ]
        self.vis = [False]*N

    def add_edge(self, first_node, second_node):
        if first_node < self.size and second_node < self.size:
            self.E[first_node].append(second_node)

    def add_double_edge(self, first_node, second_node):
        if first_node < self.size and second_node < self.size:
            self.E[first_node].append(second_node)
            self.E[second_node].append(first_node)

    def add_edges(self, edges_list):
        for begin, end in edges_list:
            self.add_edge(begin, end)

    def inner_dfs(self, node, action):
        action(node)
        for end in self.E[node]:
            if self.vis[end] == False:
                self.vis[end] = True
                self.inner_dfs(end, action)

    def dfs(self, start, action = lambda n: print(n) ):
        for i in range(self.size): self.vis[i] = False

        self.inner_dfs(start, action)

    def bfs(self, start, action = lambda n: print(n) ):
        for i in range(self.size): self.vis[i] = False
        
        q = [start]

        while not len(q) == 0:
            node = q.pop(0)
            if self.vis[node]: continue

            self.vis[node] = True
            action(node)

            for end in self.nodes[node]:
                if self.vis[end] == False:
                    q.append(end)

    def dijkstra():
		Q = PriorityQueue()
		d = [ float('inf') ] * self.size
		P = [ -1 ] * self.size

		def relax(A, a, w):
			if d[a] > d[A] + w:
				d[a] = d[A] + w
				P[a] = A
				Q.put((d[a], a))

		d[s] = 0
		for i in range(self.size):
			Q.put((d[i], i))

		while not Q.empty():
			dv, v = Q.get()
			for i in range(len(self.E[v])):
				relax(v, self.E[v][i].end, self.E[v][i].wage)
	
	def 
		

    def kruskal():
    def prime():
    def flow():
        def topology_sort():
    def 

if __name__ == "__main__":
    G = Graph(10)
    G.add_edges([[0,1],[1,2],[2,3],[3,4],[4,5],[0,6],[6,7],[6,8],[3,9]])

    
        
        
