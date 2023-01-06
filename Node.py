class Node:
    def __init__(self, value, depth=None, child=[]) -> None:
        self.depth = depth
        self.value = value
        self.children = child