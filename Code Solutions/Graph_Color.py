colors = ['Red', 'Green','Blue']
nodes = ['WA','NT','SA','Q','NSW','V','T']

neighbours = {
    'WA':['NT','SA'],
    'NT':['WA','SA','Q'],
    'SA':['WA','NT','Q','NSW','V'],
    'Q':['NT','SA','NSW'],
    'NSW':['SA','Q','V'],
    'V':['NSW','SA'],
    'T':[]
}

colors_of_nodes = {}


def promissing(node, color):
    for neighbour in neighbours[node]:
        color_of_neighbour = colors_of_nodes.get(neighbour)
        if color_of_neighbour == color:
            return False
    return True


def get_color_for_node(node):
    for color in colors:
        if promissing(node, color):
            return color


def main():
    for node in nodes:
        colors_of_nodes[node] = get_color_for_node(node)

    print(colors_of_nodes)


main()