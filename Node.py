class Node:
    def __init__(self, value, boxes=[], current_moves = [], depth=None, child=[]) -> None:
        self.depth = depth
        self.value = value
        self.boxes = boxes
        self.children = child