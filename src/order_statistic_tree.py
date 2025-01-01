class OSTNode:
    def __init__(self, key, color="R"):
        self.key = key
        self.color = color
        self.size = 1
        self.left = None
        self.right = None
        self.parent = None


class OrderStatisticTree:
    def __init__(self):
        self.NIL = OSTNode(None, color="B")
        self.NIL.size = 0
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL

    def _update_size(self, node):
        if node != self.NIL:
            node.size = node.left.size + node.right.size + 1

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        y.size = x.size
        self._update_size(x)

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        y.size = x.size
        self._update_size(x)

    def _rb_insert_fixup(self, z):
        while z.parent.color == "R":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "R":
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "R":
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self._left_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = "B"

    def insert(self, key):
        z = OSTNode(key)
        z.left = self.NIL
        z.right = self.NIL
        z.parent = self.NIL
        y = self.NIL
        x = self.root
        while x != self.NIL:
            x.size += 1
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.color = "R"
        z.size = 1
        self._rb_insert_fixup(z)

    def _rb_transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _tree_minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _rb_delete_fixup(self, x):
        while x != self.root and x.color == "B":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "R":
                    w.color = "B"
                    x.parent.color = "R"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "B" and w.right.color == "B":
                    w.color = "R"
                    x = x.parent
                else:
                    if w.right.color == "B":
                        w.left.color = "B"
                        w.color = "R"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "B"
                    w.right.color = "B"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "R":
                    w.color = "B"
                    x.parent.color = "R"
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "B" and w.left.color == "B":
                    w.color = "R"
                    x = x.parent
                else:
                    if w.left.color == "B":
                        w.right.color = "B"
                        w.color = "R"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "B"
                    w.left.color = "B"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "B"

    def delete(self, key):
        z = self.root
        while z != self.NIL:
            if z.key == key:
                break
            elif key < z.key:
                z = z.left
            else:
                z = z.right
        if z == self.NIL:
            return
        node = z.parent
        while node != self.NIL:
            node.size -= 1
            node = node.parent
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self._tree_minimum(z.right)
            y_original_color = y.color
            node = y.parent
            while node != self.NIL:
                node.size -= 1
                node = node.parent
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            y.size = z.size
            self._update_size(y.left)
            self._update_size(y.right)
        if y_original_color == "B":
            self._rb_delete_fixup(x)

    def select(self, rank):
        return self._select(self.root, rank)

    def _select(self, node, rank):
        if node == self.NIL:
            return None
        left_size = node.left.size
        if rank == left_size + 1:
            return node.key
        elif rank <= left_size:
            return self._select(node.left, rank)
        else:
            return self._select(node.right, rank - left_size - 1)

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        rank_val = 0
        current = node
        while current != self.NIL:
            if key < current.key:
                current = current.left
            else:
                rank_val += current.left.size + 1
                if key == current.key:
                    return rank_val
                current = current.right
        return rank_val

    def search(self, key):
        node = self.root
        while node != self.NIL:
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False
