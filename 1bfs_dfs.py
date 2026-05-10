from collections import deque
import threading


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Undirected graph

    # 🔵 Parallel BFS
    def parallel_bfs(self, start):
        visited = [False] * self.V
        q = deque()

        lock = threading.Lock()

        visited[start] = True
        q.append(start)

        print("\nParallel BFS Traversal:", end=" ")

        while q:
            node = q.popleft()
            print(node, end=" ")

            for neighbor in self.adj[node]:
                with lock:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

        print()

    # 🔴 DFS Utility
    def dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    # 🔴 DFS
    def parallel_dfs(self, start):
        visited = [False] * self.V

        print("\nParallel DFS Traversal:", end=" ")
        self.dfs_util(start, visited)
        print()


# Driver Code
if __name__ == "__main__":

    V = int(input("Enter number of vertices: "))
    g = Graph(V)

    E = int(input("Enter number of edges: "))

    print("Enter edges (u v):")

    for _ in range(E):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start = int(input("Enter starting vertex: "))

    g.parallel_bfs(start)
    g.parallel_dfs(start)