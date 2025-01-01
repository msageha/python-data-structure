class BPlusLeafNode:
    def __init__(self, max_keys=4):
        self.keys = []
        self.values = []
        self.next_leaf = None
        self.parent = None
        self.max_keys = max_keys

    def is_leaf(self):
        return True


class BPlusInternalNode:
    def __init__(self, max_children=4):
        self.keys = []
        self.children = []
        self.parent = None
        self.max_children = max_children

    def is_leaf(self):
        return False


class BPlusTree:
    def __init__(self, max_order=4):
        self.root = BPlusLeafNode(max_keys=max_order)
        self.max_order = max_order

    def search(self, key):
        leaf = self._find_leaf(self.root, key)
        for i, k in enumerate(leaf.keys):
            if k == key:
                return leaf.values[i]
        return None

    def insert(self, key, value):
        leaf = self._find_leaf(self.root, key)
        # 既存キーなら上書き
        for i, k in enumerate(leaf.keys):
            if k == key:
                leaf.values[i] = value
                return
        self._insert_in_leaf(leaf, key, value)

    def delete(self, key):
        leaf = self._find_leaf(self.root, key)
        if key not in leaf.keys:
            return
        idx = leaf.keys.index(key)
        leaf.keys.pop(idx)
        leaf.values.pop(idx)

        self._rebalance_after_delete(leaf)

    def _find_leaf(self, node, key):
        if node.is_leaf():
            return node
        for i, k in enumerate(node.keys):
            if key < k:
                return self._find_leaf(node.children[i], key)
        return self._find_leaf(node.children[-1], key)

    def _insert_in_leaf(self, leaf, key, value):
        insert_idx = 0
        while insert_idx < len(leaf.keys) and leaf.keys[insert_idx] < key:
            insert_idx += 1
        leaf.keys.insert(insert_idx, key)
        leaf.values.insert(insert_idx, value)

        if len(leaf.keys) > leaf.max_keys:
            self._split_leaf(leaf)

    def _split_leaf(self, leaf):
        new_leaf = BPlusLeafNode(max_keys=leaf.max_keys)
        new_leaf.parent = leaf.parent

        mid = (len(leaf.keys) + 1) // 2
        new_leaf.keys = leaf.keys[mid:]
        new_leaf.values = leaf.values[mid:]
        leaf.keys = leaf.keys[:mid]
        leaf.values = leaf.values[:mid]

        new_leaf.next_leaf = leaf.next_leaf
        leaf.next_leaf = new_leaf

        new_key = new_leaf.keys[0]
        self._insert_in_parent(leaf, new_key, new_leaf)

    def _insert_in_parent(self, left_node, new_key, right_node):
        parent = left_node.parent

        if parent is None:
            new_root = BPlusInternalNode(max_children=self.max_order)
            new_root.keys = [new_key]
            new_root.children = [left_node, right_node]
            left_node.parent = new_root
            right_node.parent = new_root
            self.root = new_root
            return

        insert_idx = 0
        while insert_idx < len(parent.keys) and parent.keys[insert_idx] < new_key:
            insert_idx += 1

        parent.keys.insert(insert_idx, new_key)
        parent.children.insert(insert_idx + 1, right_node)
        right_node.parent = parent

        if len(parent.children) > parent.max_children:
            self._split_internal(parent)

    def _split_internal(self, internal):
        new_internal = BPlusInternalNode(max_children=internal.max_children)
        new_internal.parent = internal.parent

        mid = len(internal.keys) // 2

        new_internal.keys = internal.keys[mid + 1 :]
        new_internal.children = internal.children[mid + 1 :]

        up_key = internal.keys[mid]

        internal.keys = internal.keys[:mid]
        internal.children = internal.children[: mid + 1]

        for c in new_internal.children:
            c.parent = new_internal

        self._insert_in_parent(internal, up_key, new_internal)

    def _rebalance_after_delete(self, node):
        if node == self.root:
            if node.is_leaf():
                if len(node.keys) == 0:
                    pass
            else:
                if len(node.keys) == 0:
                    self.root = node.children[0]
                    self.root.parent = None
            return

        min_keys = (
            (node.max_keys + 1) // 2 - 1
            if node.is_leaf()
            else (node.max_children + 1) // 2 - 1
        )
        if len(node.keys) >= min_keys:
            return

        parent = node.parent
        idx = parent.children.index(node)

        if idx > 0:
            left_sibling = parent.children[idx - 1]
        else:
            left_sibling = None
        if idx < len(parent.children) - 1:
            right_sibling = parent.children[idx + 1]
        else:
            right_sibling = None

        if right_sibling:
            self._merge_nodes(node, right_sibling, parent, idx)
        elif left_sibling:
            self._merge_nodes(left_sibling, node, parent, idx - 1)

    def _merge_nodes(self, left_node, right_node, parent, parent_key_idx):
        if left_node.is_leaf():
            left_node.keys.extend(right_node.keys)
            left_node.values.extend(right_node.values)
            left_node.next_leaf = right_node.next_leaf
        else:
            merge_key = parent.keys[parent_key_idx]
            left_node.keys.append(merge_key)
            left_node.keys.extend(right_node.keys)
            for child in right_node.children:
                child.parent = left_node
            left_node.children.extend(right_node.children)

        parent.keys.pop(parent_key_idx)
        parent.children.pop(parent_key_idx + 1)

        if parent == self.root and len(parent.keys) == 0:
            self.root = left_node
            left_node.parent = None
