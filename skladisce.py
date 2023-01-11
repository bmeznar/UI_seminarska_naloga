class Skladisce:
    def __init__(self, boxes, p, n):
        self.boxes = boxes
        self.p = p-1
        self.n = n-1

    def prestavi(self, p, r):
        if p <= self.p or r <= self.p :

            i = 0
            box = ' '
            while self.boxes[i][p] == ' ':
                if i >= self.n:
                    break;
                i += 1
            box = self.boxes[i][p]
            self.boxes[i][p] = ' '
            if box != ' ':
                j = 0
                while self.boxes[j][r] == ' ':
                    j += 1
                    if j > self.n:
                        break;
                j -= 1
                if j >= 0:
                    self.boxes[j][r] = box
                    return 0
                else:
                    self.boxes[i][p] = box
                    #print("Stack is already full")
                    return 1
        else:
            #print("Wrong indexes")
            return 1

    def print(self):
        for height in self.boxes:
            print(height)
