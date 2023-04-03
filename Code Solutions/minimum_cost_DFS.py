visited = []
Nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'P']
AdjList = {
    "S": ["A", "D"],
    "A": ["S", "B", "C"],
    "B": ["A", "C", "P"],
    "C": ["A", "B", "D", "E"],
    "D": ["S", "C", "E"],
    "E": ["C", "D", "P"],
    "P": ["B", "E"]
}
weight = {
    "SA": 5,
    "AS": 5,
    "BA": 9,
    "AB": 9,
    "BP": 7,
    "PB": 7,
    "EP": 4,
    "PE": 4,
    "DE": 6,
    "ED": 6,
    "SD": 8,
    "DS": 8,
    "AC": 3,
    "CA": 3,
    "DC": 4,
    "CD": 4,
    "CE": 2,
    "EC": 2,
    "BC": 5,
    "CB": 5
}
SumOfWight = []
AllPath = []
Start = input("Enter staring node: ").upper()
Destination = input("Enter destination node: ").upper()


# Main DFS function
def StartDFS(item):
    visited.append(item)
    for value in AdjList[item]:
        if value not in visited:
            if value == Destination:
                path = visited[0::]
                path.append(value)
                AllPath.append(path)
                print(f'Path: {path}')
            StartDFS(value)
            visited.remove(value)

StartDFS(Start)

sum = 0
for items in AllPath:
    Pre = items[0]
    for value in range(1, len(items)):
        String = Pre + items[value]
        sum += weight[String]
        Pre = items[value]
    SumOfWight.append(sum)
    sum = 0
print(f"All cost: {SumOfWight}")
PathIndex = SumOfWight.index(min(SumOfWight))
print(f"Shortest Path: {AllPath[PathIndex]}")
