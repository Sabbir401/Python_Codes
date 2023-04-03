adj_list = {
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


# Required DS

color = {} # W G B
parent = {} # Path

time = 0
time_tracking = {} # Node -> [t1, t2]
output = [] # Traversal Sequence

# Initialization
for node in adj_list.keys():
  color[node] = 'W'
  parent[node] = None
  time_tracking[node] = [-1, -1]

def DFS(u):
  global time
  color[u] = 'G'
  time_tracking[u][0] = time
  time += 1
  output.append(u)

  for v in adj_list[u]:
    if color[v] == 'W':
      parent[u] = v
      DFS(v)
    elif color[v] == 'B' and parent[v] != u:
        print('Cycle Detected')

  color[u] = 'B'
  time_tracking[u][1] = time
  time += 1

DFS('A')

print('Color: ', color)
print('Parent: ', parent)
print('Time Tracking: ', time_tracking)
print('Output: ', output)

# if flag == 1:
#     print('Cycle Detected')
# else:
#     print('No Cycle')