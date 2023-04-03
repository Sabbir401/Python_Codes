WhatIVisit=[]
LoopCount=0
Parent={}
Nodes=input("Enter all nodes using comma:").upper().split(",")

#Parent Assign
for Node in Nodes:
    Parent[Node]=""
#Adj List Value Assign
AdjList = {
    'A': ['B', 'C'],
    'B': ['A', 'D','E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B','H','I'],
    'F': ['C'],
    'G': ['C','J'],
    'H': ['E'],
    'I': ['E']
}
#Main DFS function
def StartDFS(item):
    global LoopCount
    WhatIVisit.append(item)
    for value in AdjList[item]:
        if value not in WhatIVisit:
            Parent[value]=item
            StartDFS(value)
        else: 
            print(f'For {item}')
            if Parent[item]!=value:
                print(WhatIVisit)
                LoopCount+=1
                print(LoopCount)


Start=input("Enter staring node: ").upper()
Parent[Start]=""
StartDFS(Start)
print("______________")
for item in Nodes:
    if item not in WhatIVisit:
        StartDFS(item)

print(WhatIVisit)
print(Parent)
print(f"{LoopCount} loop found")