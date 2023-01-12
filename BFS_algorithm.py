from skladisce import Skladisce
from Node import Node
import copy

P = 4   #št. stolpcev v skladišču
N = 4   #višina skladišča
arr = [ [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        ['E','F',' ',' '],
        ['A','C','D','B'] ]

final = Skladisce([ [' ',' ',' ',' '],
                    [' ',' ',' ',' '],
                    ['D','E',' ','C'],
                    ['B','A',' ','F'] ], P, N)

out = Skladisce(copy.deepcopy(arr), P, N)

skladisce_1 = Skladisce(copy.deepcopy(arr), P, N)


stack_indexes = list(range(0, P, 1))

#node_index = 0
out = Skladisce(copy.deepcopy(arr), P, N)

def all_options():
    nodes = []
    for i in range(0, len(stack_indexes)):
        for j in range(0, len(stack_indexes)):
            if (i != j):
                nodes.append((stack_indexes[i], stack_indexes[j]))
    return nodes


possible_moves = all_options()
possible_moves.insert(0, (0,0))

depth = P * N

def build_graph(depth, index, steps, current_position):

    if depth == 0:
        premik = possible_moves[index]
        pomozni_koraki = steps
        pomozno_skladisce = copy.deepcopy(current_position)
        return Node(premik, pomozno_skladisce.boxes, pomozni_koraki)

    children = []
    for i in range(1, len(possible_moves)):
        premik = possible_moves[i]
        pomozno_skladisce = copy.deepcopy(current_position)
        mozen_premik = pomozno_skladisce.prestavi(premik[0], premik[1])
        if len(steps) > 0:
            if mozen_premik == 0 and (premik[1], premik[0]) != steps[-1] and pomozno_skladisce.boxes != current_position.boxes :
                pomozni_koraki = copy.deepcopy(steps)
                pomozni_koraki.append(premik)
                children.append(build_graph(depth-1, i, pomozni_koraki, pomozno_skladisce))
        else:
            if mozen_premik == 0 and pomozno_skladisce.boxes != current_position.boxes :
                pomozni_koraki = copy.deepcopy(steps)
                pomozni_koraki.append(premik)
                children.append(build_graph(depth-1, i, pomozni_koraki, pomozno_skladisce))

    premik = possible_moves[index]
    pomozni_koraki = steps
    pomozno_skladisce = copy.deepcopy(current_position)
    return Node(premik, pomozno_skladisce.boxes, pomozni_koraki, depth, children)


fastest_node = None

queue = []
visited = []
def bfs_algorithm(visited, node):
    global fastest_node
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)

        for children in m.children:
            if children not in visited:
                if children.boxes == final.boxes:
                    fastest_node = children
                    return
                visited.append(children)
                queue.append(children)




graph = build_graph(depth, 0, [], out)
print("graph built")
bfs_algorithm(visited, graph)

print("Število potrebnih korakov: " + str(len(fastest_node.current_moves)))
print(fastest_node.current_moves)



