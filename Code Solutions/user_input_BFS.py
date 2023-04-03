from queue import Queue

Nodes = input("Enter all nodes:").upper().split()
adj_List = {}
for i in Nodes:
    neighbor = input(f'Enter nodes for {i}: ')
    if neighbor:
        adj_List[i] = neighbor.upper().split()
    else:
        adj_List[i] = []
print(adj_List)

parent={}
level={}
visited={}
output=[]
queue=Queue()
for node in adj_List.keys():
    visited[node]=False
    level[node]=-1
    parent[node]=None

s=input("Enter Root Node: ").upper()
visited[s]=True
level[s]=0
queue.put(s)

while not queue.empty():
    u=queue.get()
    output.append(u)
    for v in adj_List[u]:
        if not visited[v]:
            queue.put(v)
            visited[v]=True
            level[v]=level[u]+1
            parent[v]=u
print(output)
print(level)
print(parent)