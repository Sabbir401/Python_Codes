WhatIVisit=[]
Level={}
Nodes=input("Enter all nodes using comma:").upper().split(",")
AdjList={}
flag=0
#Level Assign
for Node in Nodes:
    Level[Node]=-1

#Adj List Value Assign
for item in Nodes:
    ConnValues=input(f'Enter nodes for {item} using ",": ')
    if ConnValues:
        AdjList[item]=ConnValues.upper().split(',')
    else:
        AdjList[item]=[]

Start=input("Enter staring node: ").upper()
destination=input("Enter destination:").upper()
WhatLevel=int(input("Enter level:"))

#Main DFS function
def StartDFS(item):
    global flag
    WhatIVisit.append(item)
    if item==destination and Level[item]<=WhatLevel:
        flag=1
        print(f"{item} found level: {Level[item]}")
    elif flag==0:
        for value in AdjList[item]:
            if value not in WhatIVisit:
                Level[value]=Level[item]+1
                if value==destination and Level[value]<=WhatLevel:
                    flag=1
                    print(f"{value} found level: {Level[value]}")
                    break
                elif Level[value]<=WhatLevel:
                    StartDFS(value)

Level[Start]=0
StartDFS(Start)
