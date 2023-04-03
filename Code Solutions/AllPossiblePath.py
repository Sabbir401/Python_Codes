visited=[]
AdjList = {
    "S": ["A", "D"],
    "A": ["S", "B", "C"],
    "B": ["A", "C", "P"],
    "C": ["A", "B", "D", "E"],
    "D": ["S", "C", "E"],
    "E": ["C", "D", "P"],
    "P": ["B", "E"]
}
Start=input("Enter staring node: ").upper()
Destination=input("Enter destination node: ").upper()
#Main DFS function
def DFS(item):
    visited.append(item)
    for value in AdjList[item]:
        if value not in visited:
            if value==Destination:
                path=visited[0::]
                path.append(value)
                print(f'Path: {path}')
            DFS(value)
            visited.remove(value)
DFS(Start)