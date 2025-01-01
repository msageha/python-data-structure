class MultiSetNode:
    def __init__(self, key, color="R"):
        self.key = key
        self.count = 1
        self.color = color
        self.size = 1
        self.left = None
        self.right = None
        self.parent = None


class TreeBasedMultiset:
    def __init__(self):
        self.NIL = MultiSetNode(None, color="B")
        self.NIL.count = 0
        self.NIL.size = 0
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL

    def _update_size(self, node):
        if node != self.NIL:
            node.size = node.left.size + node.right.size + node.count

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
        y = self.NIL
        x = self.root
        while x != self.NIL:
            x.size += 1
            y = x
            if key == x.key:
                x.count += 1
                return
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        z = MultiSetNode(key)
        z.left = self.NIL
        z.right = self.NIL
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.color = "R"
        z.size = z.count
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
                        w.left.color = "R"
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
                        w.right.color = "R"
                        w.color = "R"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "B"
                    w.left.color = "B"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "B"

    def remove(self, key):
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
        if z.count > 1:
            z.count -= 1
            node = z
            while node != self.NIL:
                node.size -= 1
                node = node.parent
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
            y.count = z.count
            y.size = z.size
        if y_original_color == "B":
            self._rb_delete_fixup(x)

    def count(self, key):
        current = self.root
        while current != self.NIL:
            if key == current.key:
                return current.count
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return 0

    def size(self):
        return self.root.size

    def search(self, key):
        current = self.root
        while current != self.NIL:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def _inorder(self, node, res):
        if node == self.NIL:
            return
        self._inorder(node.left, res)
        for _ in range(node.count):
            res.append(node.key)
        self._inorder(node.right, res)

    def to_list(self):
        r = []
        self._inorder(self.root, r)
        return r
