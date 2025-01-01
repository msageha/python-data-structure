class DLXNode:
    def __init__(self, c=None):
        self.L = self
        self.R = self
        self.U = self
        self.D = self
        self.C = c


class DLXColumn(DLXNode):
    def __init__(self, name=""):
        super().__init__()
        self.size = 0
        self.name = name


class DancingLinks:
    def __init__(self, matrix, col_names=None):
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0]) if self.n_rows > 0 else 0
        self.sol = []
        self.header = DLXColumn()
        self.header.L = self.header
        self.header.R = self.header
        self.columns = []
        for i in range(self.n_cols):
            c = DLXColumn(name=str(i) if not col_names else col_names[i])
            c.L = self.header.L
            c.R = self.header
            self.header.L.R = c
            self.header.L = c
            self.columns.append(c)
        for r in range(self.n_rows):
            first_node = None
            for c in range(self.n_cols):
                if matrix[r][c] == 1:
                    col = self.columns[c]
                    new_node = DLXNode(c=col)
                    if first_node is None:
                        first_node = new_node
                    new_node.U = col.U
                    new_node.D = col
                    col.U.D = new_node
                    col.U = new_node
                    if first_node != new_node:
                        new_node.L = first_node.L
                        new_node.R = first_node
                        first_node.L.R = new_node
                        first_node.L = new_node
                    col.size += 1

    def cover(self, col):
        col.R.L = col.L
        col.L.R = col.R
        row = col.D
        while row != col:
            node = row.R
            while node != row:
                node.U.D = node.D
                node.D.U = node.U
                node.C.size -= 1
                node = node.R
            row = row.D

    def uncover(self, col):
        row = col.U
        while row != col:
            node = row.L
            while node != row:
                node.C.size += 1
                node.U.D = node
                node.D.U = node
                node = node.L
            row = row.U
        col.R.L = col
        col.L.R = col

    def search(self, k=0):
        if self.header.R == self.header:
            yield [n.C.name for n in self.sol]
        else:
            c = None
            s = 999999999
            col = self.header.R
            while col != self.header:
                if col.size < s:
                    c = col
                    s = col.size
                col = col.R
            self.cover(c)
            row = c.D
            while row != c:
                self.sol.append(row)
                right_node = row.R
                while right_node != row:
                    self.cover(right_node.C)
                    right_node = right_node.R
                for solution in self.search(k + 1):
                    yield solution
                left_node = row.L
                while left_node != row:
                    self.uncover(left_node.C)
                    left_node = left_node.L
                self.sol.pop()
                row = row.D
            self.uncover(c)

    def solve(self):
        for sol in self.search():
            yield sol
