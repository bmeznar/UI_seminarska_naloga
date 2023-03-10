from collections import deque

from skladisce import Skladisce
from Node import Node
import copy

P = 3   #št. stolpcev v skladišču
N = 3   #višina skladišča
arr = [ [' ',' ',' '],
        [' ',' ',' '],
        ['A','B','C'] ]

final = Skladisce([ ['A',' ',' '],
                    ['C',' ',' '],
                    ['B',' ',' '] ], P, N)

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
        if mozen_premik == 0 and pomozno_skladisce.boxes != current_position.boxes :
            pomozni_koraki = copy.deepcopy(steps)
            pomozni_koraki.append(premik)
            children.append(build_graph(depth-1, i, pomozni_koraki, pomozno_skladisce))

    premik = possible_moves[index]
    pomozni_koraki = steps
    pomozno_skladisce = copy.deepcopy(current_position)
    return Node(premik, pomozno_skladisce.boxes, pomozni_koraki, depth, children)


fastest_node = None
visited = []
end = False
nodecount = 0
enddepth = 0

def iddfs_algorithm(visited, node, depthLimit):
    global fastest_node, nodecount, end
    nodecount += 1
    if node not in visited:
        visited.append(node)
    if node.boxes == final.boxes:
        if fastest_node == None or len(node.current_moves) < len(fastest_node.current_moves):
            fastest_node = node
        end = True
        return True
    if depthLimit <= 0:
        return False
    for children in node.children:
       if iddfs_algorithm(visited, children, depthLimit - 1):
           return True
    return False

def iddfsgen(visited, currNode, maxDepth):
    global enddepth, end

    for x in range(P * N):
        iddfs_algorithm(visited, currNode, x)
        if end:
            enddepth = x
            return



graph = build_graph(depth, 0, [], out)

iddfsgen(visited, graph, P*N)

print("Število potrebnih korakov: " + str(len(fastest_node.current_moves)))
print(fastest_node.current_moves)
print("Število obdelanih vozlišč: " + str(nodecount))
print("Največja preiskana globina: " + str(enddepth))
