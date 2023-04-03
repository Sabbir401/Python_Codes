Nodes=input("Enter your all nodes using comma ',': ").split(",")
AdjList={}
usedColor={}
for node in Nodes:
    AdjList[node]=input(f"{node}: ").split(",")

for node in Nodes:
    usedColor[node]=None

m=int(input("Enter how many color: "))
color=[0 for i in range (m)]
colors=["Red","Green","Blue","Black","white","purple"]
def checkColor(node):
    if usedColor[node] != None:
        color[usedColor[node]]=1

for i in AdjList.keys():
    for j in AdjList[i]:
        checkColor(j)
    for index, value in enumerate(color):
        if value == 0:
            usedColor[i]=index
            for m in range(len(color)):
                color[m]=0
            break
if None in usedColor.values():
    print("Color not possible")
else:
    for i in zip(usedColor.keys(),usedColor.values()):
        print(f'{i[0]} -> {colors[i[1]]}')