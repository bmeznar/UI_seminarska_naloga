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

out = Skladisce(copy.deepcopy(arr), P, N)

preiskana_vozlisca = 0
preiskana_globina = 0
stevilo_vseh_vozlisc = 0

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
    global stevilo_vseh_vozlisc

    if depth == 0:
        premik = possible_moves[index]
        pomozni_koraki = steps
        pomozno_skladisce = copy.deepcopy(current_position)
        stevilo_vseh_vozlisc += 1
        return Node(premik, pomozno_skladisce.boxes, pomozni_koraki)

    children = []
    for i in range(1, len(possible_moves)):
        premik = possible_moves[i]
        pomozno_skladisce = copy.deepcopy(current_position)
        mozen_premik = pomozno_skladisce.prestavi(premik[0], premik[1])
        if len(steps) > 0:
            if mozen_premik == 0 and (premik[1], premik[0]) != steps[-1] and pomozno_skladisce.boxes != current_position.boxes:
                pomozni_koraki = copy.deepcopy(steps)
                pomozni_koraki.append(premik)
                children.append(build_graph(depth - 1, i, pomozni_koraki, pomozno_skladisce))
        else:
            if mozen_premik == 0 and pomozno_skladisce.boxes != current_position.boxes:
                pomozni_koraki = copy.deepcopy(steps)
                pomozni_koraki.append(premik)
                children.append(build_graph(depth - 1, i, pomozni_koraki, pomozno_skladisce))

    premik = possible_moves[index]
    pomozni_koraki = steps
    pomozno_skladisce = copy.deepcopy(current_position)
    stevilo_vseh_vozlisc += 1
    return Node(premik, pomozno_skladisce.boxes, pomozni_koraki, depth, children)


fastest_node = None
visited = []

def dfs_algorithm(visited, node):
    global fastest_node, preiskana_vozlisca, preiskana_globina
    if node not in visited:
        preiskana_vozlisca += 1
        visited.append(node)
        if len(node.current_moves) > preiskana_globina:
            preiskana_globina = len(node.current_moves)
        if node.boxes == final.boxes:
            if fastest_node == None or len(node.current_moves) < len(fastest_node.current_moves):
                fastest_node = node
            return 0
        elif fastest_node != None and len(node.current_moves) >= len(fastest_node.current_moves):
            return 0
        for children in node.children:
            dfs_algorithm(visited, children)




graph = build_graph(depth, 0, [], out)
#print("graph built")
dfs_algorithm(visited, graph)

print("Število potrebnih korakov: " + str(len(fastest_node.current_moves)))
print(fastest_node.current_moves)

print("Vsa vozlišča: " + str(stevilo_vseh_vozlisc))
print("Število preiskanih vozlišč: " + str(preiskana_vozlisca))
print("Največja preiskana globina: " + str(preiskana_globina))

