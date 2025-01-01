class RopeNode:
    def __init__(self, s):
        self.left = None
        self.right = None
        self.s = s
        self.weight = len(s) if s else 0


def _update_weight(node):
    if node:
        node.weight = (node.left.weight if node.left else 0) + (
            len(node.s) if node.s else 0
        )


def _split(node, idx):
    if not node:
        return None, None
    if node.left:
        left_weight = node.left.weight
    else:
        left_weight = 0
    cur_len = left_weight + (len(node.s) if node.s else 0)
    if idx < left_weight:
        l, r = _split(node.left, idx)
        node.left = r
        _update_weight(node)
        return l, node
    elif idx > left_weight and idx < cur_len:
        split_point = idx - left_weight
        left_part = RopeNode(node.s[:split_point])
        right_part = RopeNode(node.s[split_point:])
        left_part.left = node.left
        _update_weight(left_part)
        node.s = right_part.s
        node.left = None
        _update_weight(node)
        return left_part, node
    elif idx == left_weight:
        l = node.left
        node.left = None
        _update_weight(node)
        return l, node
    else:
        idx2 = idx - cur_len
        l, r = _split(node.right, idx2)
        node.right = l
        _update_weight(node)
        return node, r


def _concat(left_node, right_node):
    if not left_node:
        return right_node
    if not right_node:
        return left_node
    cur = left_node
    while cur.right:
        cur = cur.right
    cur.right = right_node
    _update_weight(cur)
    return left_node


def _length(node):
    if not node:
        return 0
    return (
        (node.left.weight if node.left else 0)
        + (len(node.s) if node.s else 0)
        + _length(node.right)
    )


def _index(node, idx):
    if not node:
        return None
    left_weight = node.left.weight if node.left else 0
    if idx < left_weight:
        return _index(node.left, idx)
    if node.s and idx < left_weight + len(node.s):
        return node.s[idx - left_weight]
    return _index(node.right, idx - left_weight - (len(node.s) if node.s else 0))


def _build_rope(s):
    return RopeNode(s)


class Rope:
    def __init__(self, s=""):
        self.root = _build_rope(s)

    def insert(self, idx, s):
        left_part, right_part = _split(self.root, idx)
        new_node = _build_rope(s)
        merged_left = _concat(left_part, new_node)
        self.root = _concat(merged_left, right_part)

    def remove(self, start, length):
        left_part, temp = _split(self.root, start)
        _, right_part = _split(temp, length)
        self.root = _concat(left_part, right_part)

    def substring(self, start, length):
        l, temp = _split(self.root, start)
        m, r = _split(temp, length)
        res = []
        self._traverse_collect(m, res)
        self.root = _concat(l, _concat(m, r))
        return "".join(res)

    def _traverse_collect(self, node, res):
        if not node:
            return
        self._traverse_collect(node.left, res)
        if node.s:
            res.append(node.s)
        self._traverse_collect(node.right, res)

    def index(self, idx):
        return _index(self.root, idx)

    def length(self):
        return _length(self.root)

    def to_string(self):
        res = []
        self._traverse_collect(self.root, res)
        return "".join(res)
