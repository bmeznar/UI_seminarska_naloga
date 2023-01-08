from skladisce import Skladisce
from Node import Node
import copy
import sys
sys.setrecursionlimit(10**6)

P = 3   #št. stolpcev v skladišču
N = 3   #višina skladišča
arr = [ [' ',' ',' '],
        ['B','E',' '],
        ['A','C','D']]

skladisce_1 = Skladisce(copy.deepcopy(arr), P, N)


stack_indexes = list(range(0, P, 1))

node_index = 0

def all_options():
    nodes = []
    for i in range(0, len(stack_indexes)):
        for j in range(0, len(stack_indexes)):
            if (i != j):
                nodes.append((stack_indexes[i], stack_indexes[j]))
    return nodes

possible_moves = all_options()
possible_moves.insert(0, (0,0))


depth = 3

def build_graph(depth, index):
    global first_node
    if depth == 0:
        return Node(possible_moves[index])
    children = [build_graph(depth - 1, i) for i in range(1, len(possible_moves))]
    return Node(possible_moves[index], depth, children)


final = Skladisce([[' ','B',' '],
                   [' ','A',' ']], P, N)

out = Skladisce(copy.deepcopy(arr), P, N)

fastest_steps = -1
current_steps = 0
fastest_moves = []
current_moves = []

visited = []    #obiskani nodi za trenutno rekurzijo
finished_visited = []   #obiskani nodi koncanih obhodov


def iddfs_algorithm(visited, node, out):
    global current_steps, current_moves, fastest_steps, fastest_moves

    for x in range(P * N):
        for child in node.children:
            if child not in visited:
                out.prestavi(child.value[0], child.value[1])
                current_steps += 1
                current_moves.append(child.value)
                if out.boxes == final.boxes:
                    if current_steps < fastest_steps or fastest_steps == -1:
                        fastest_steps = current_steps
                        fastest_moves = current_moves
                else:
                    dfs_algorithm(visited, child, out)
                break

        if node not in visited:
            visited.append(node)
            if graph not in visited:
                out = Skladisce(copy.deepcopy(arr), P, N)
                current_steps = 0
                current_moves = []
                dfs_algorithm(visited, graph, out)



graph = build_graph(depth, 0)
iddfs_algorithm(visited, graph, out)
print(fastest_moves)