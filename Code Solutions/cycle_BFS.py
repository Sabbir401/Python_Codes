# Adjacency List

adj_list={
     'A': ['B', 'F'],
    'B': ['A','C', 'D'],
    'D': ['B','E'],
    'E': ['D','C'],
    'C': ['B','E'],
    'F': ['A', 'G'],
    'G': ['F', 'H', 'I'],
    'I': ['J','G'],
    'H': ['G'],
    'J': ['I']
}
# Initialization
from queue import Queue

visited = {}
level = {}
parent = {}

output = []
queue = Queue()

for node in adj_list.keys():
  visited[node] = False
  level[node] = -1
  parent[node] = None


# selecting root
s = 'A'
visited[s] = True
level[s] = 0
queue.put(s)



# BFS Implementation
flag=0
while not queue.empty():
  u = queue.get()
  output.append(u)

  for v in adj_list[u]:
    if not visited[v]:
      queue.put(v)
      visited[v] = True
      level[v] = level[u] + 1
      parent[v] = u
    elif visited[u] == True and parent[u] != v:
        flag=1

if flag == 1:
    print('Cycle Detected')
else:
    print('No Cycle')

print(parent)
print(level)