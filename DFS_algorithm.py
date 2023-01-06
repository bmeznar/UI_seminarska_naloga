from skladisce import Skladisce
from Node import Node

P = 3   #št. stolpcev v skladišču
N = 3   #višina skladišča

skladisce_1 = Skladisce([[' ',' ',' '],[' ',' ',' '],['A','B','C']], P, N)


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


depth = 5
def build_graph(depth, index):
    global first_node
    if depth == 0:
        return Node(possible_moves[index])
    children = [build_graph(depth - 1, i) for i in range(1, len(possible_moves))]
    return Node(possible_moves[index], depth, children)


final = Skladisce([['A',' ',' '],['C',' ',' '],['B',' ',' ']], P, N)
out = skladisce_1

fastest_steps = -1
current_steps = 0
fastest_moves = []
current_moves = []

visited = []    #obiskani nodi za trenutno rekurzijo
finished_visited = []   #obiskani nodi koncanih obhodov

def dfs_algorithm(visited, finished_visited, node):
    global fastest_steps
    global current_steps
    global fastest_moves
    global current_moves

    visited.append(node)

    for child in node.children:

        if child not in visited and child not in finished_visited:
            move_from = child.value[0]
            move_to = child.value[1]
            out.prestavi(move_from, move_to)
            current_moves.append((move_from, move_to))
            current_steps += 1

            if current_steps > fastest_steps and fastest_steps != -1:
                visited.clear()
                finished_visited.append(child)
                current_steps = 0
                current_moves = []
                dfs_algorithm(visited, finished_visited, graph)

            elif out.boxes == final.boxes:
                visited.clear()
                finished_visited.append(child)
                fastest_moves = current_moves
                fastest_steps = current_steps
                current_steps = 0
                current_moves = []
                dfs_algorithm(visited, finished_visited, graph)

            else:
                dfs_algorithm(visited, finished_visited, child)
    finished_visited.append(node)
    #return visited




graph = build_graph(depth, 0)
dfs_algorithm(visited, finished_visited, graph)
print(fastest_moves)