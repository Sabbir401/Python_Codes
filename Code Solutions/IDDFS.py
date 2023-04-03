graph = {  # for representing graph used dictionary
    'A': ['B', 'C'],  # making edges
    'B': ['D', 'E'],  # internal node
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'G': ['M'],
    'F': ['L'],
    'H': [],  # leaf node
    'I': [],  # leaf node
    'J': [],  # leaf node
    'K': [],  # leaf node
    'L': [],  # leaf node
    'M': []  # leaf node
}

path = list()  # to store path source to dest


def DFS(c_node, dest_node, graph, maxDepth, store_list):  # recursive dfs
    print(c_node, end=" ")  # print current visited node
    store_list.append(c_node)  # store current node to temporary list
    if c_node == dest_node:
        return True  # return true if found dest node
    if maxDepth <= 0:
        path.append(store_list)
        # print(store_list)
        return False  # return false if don't found dest node and depth is 0
    for node in graph[c_node]:
        if DFS(node, dest_node, graph, maxDepth - 1, store_list):
            return True  # if DFS function return true then this statement also return true
        else:
            store_list.pop()

    return False  # when above all condition are fails, return false


def IDDFS(c_node, dest_node, graph, maxDepth):  # this func call DFS with depth limit
    for i in range(maxDepth):
        print("\n\nLevel  ", i)
        store_list = list()
        if DFS(c_node, dest_node, graph, i, store_list):
            return True

    return False


if not IDDFS('A', 'G', graph, 4):
    print("Path is not available")
else:
    print("\n\npath is ", end=" ")
    # print(path)
    print(path.pop())