WhatIVisit=[]
ValueInQueue=[]
Level={}
Parent={}
LoopCount=0
Nodes=input("Enter all nodes using comma:").upper().split(",")
#Level & Parent Assign
for Node in Nodes:
    Level[Node]=-1
    Parent[Node]=""
AdjList={}
#Adj List Value Assign
for item in Nodes:
    ConnValues=input(f'Enter nodes for {item} using ",": ')
    if ConnValues:
        AdjList[item]=ConnValues.upper().split(',')
    else:
        AdjList[item]=[]
ValueInQueue.append(input("Enter staring node: ").upper())
Level[ValueInQueue[0]]=0
Parent[ValueInQueue[0]]="None"
while(ValueInQueue):
    PopedValue=ValueInQueue.pop(0)
    if PopedValue not in WhatIVisit:
        WhatIVisit.append(PopedValue)
        for values in AdjList[PopedValue]:
            if values not in WhatIVisit:
                if values not in ValueInQueue:
                    Level[values]=Level[PopedValue]+1
                    Parent[values]=PopedValue
                ValueInQueue.append(values)
            else:
                if Parent[PopedValue]!=values:
                    LoopCount+=1
for i in WhatIVisit:
    print(i, end=" ")
if LoopCount:
    print(f'\n{LoopCount} Loop found!!')
else:
    print(f'\nNo loop!!')
print(Level)
print(Parent)