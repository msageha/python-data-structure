class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = leaf

    def __repr__(self):
        return f"<BTreeNode keys={self.keys}, leaf={self.leaf}>"


class BTree:
    def __init__(self, t=2):
        self.t = t
        self.root = BTreeNode(t=self.t, leaf=True)

    def search(self, k):
        return self._search_node(self.root, k)

    def _search_node(self, node, k):
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and k == node.keys[i]:
            return True

        if node.leaf:
            return False
        else:
            return self._search_node(node.children[i], k)

    def insert(self, k):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(t=self.t, leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, parent, idx):
        t = self.t
        node_to_split = parent.children[idx]
        new_node = BTreeNode(t=t, leaf=node_to_split.leaf)

        parent.keys.insert(idx, node_to_split.keys[t - 1])
        parent.children.insert(idx + 1, new_node)

        new_node.keys = node_to_split.keys[t : (2 * t - 1)]
        node_to_split.keys = node_to_split.keys[0 : (t - 1)]

        if not node_to_split.leaf:
            new_node.children = node_to_split.children[t : (2 * t)]
            node_to_split.children = node_to_split.children[0:t]

    def delete(self, k):
        self._delete_internal(self.root, k)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete_internal(self, node, k):
        t = self.t
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == k:
            if node.leaf:
                node.keys.pop(i)
            else:
                left_child = node.children[i]
                right_child = node.children[i + 1]
                if len(left_child.keys) >= t:
                    pred_key = self._get_predecessor(left_child)
                    node.keys[i] = pred_key
                    self._delete_internal(left_child, pred_key)
                elif len(right_child.keys) >= t:
                    succ_key = self._get_successor(right_child)
                    node.keys[i] = succ_key
                    self._delete_internal(right_child, succ_key)
                else:
                    self._merge_children(node, i)
                    self._delete_internal(left_child, k)
        else:
            if node.leaf:
                return
            child = node.children[i]
            if len(child.keys) < t:
                self._fill_child(node, i)
            if i < len(node.children):
                child = node.children[i]
            else:
                child = node.children[i - 1]
            self._delete_internal(child, k)

    def _get_predecessor(self, node):
        while not node.leaf:
            node = node.children[len(node.children) - 1]
        return node.keys[-1]

    def _get_successor(self, node):
        while not node.leaf:
            node = node.children[0]
        return node.keys[0]

    def _merge_children(self, node, idx):
        child1 = node.children[idx]
        child2 = node.children[idx + 1]

        child1.keys.append(node.keys[idx])
        child1.keys.extend(child2.keys)

        if not child1.leaf:
            child1.children.extend(child2.children)

        node.keys.pop(idx)
        node.children.pop(idx + 1)

    def _fill_child(self, node, idx):
        t = self.t
        if idx > 0 and len(node.children[idx - 1].keys) >= t:
            self._borrow_from_prev(node, idx)
        elif idx < len(node.children) - 1 and len(node.children[idx + 1].keys) >= t:
            self._borrow_from_next(node, idx)
        else:
            if idx < len(node.children) - 1:
                self._merge_children(node, idx)
            else:
                self._merge_children(node, idx - 1)

    def _borrow_from_prev(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx - 1]

        child.keys.insert(0, node.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop(len(sibling.children) - 1))

        node.keys[idx - 1] = sibling.keys.pop(len(sibling.keys) - 1)

    def _borrow_from_next(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]

        child.keys.append(node.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

        node.keys[idx] = sibling.keys.pop(0)
