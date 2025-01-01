class SuffixNode:
    def __init__(self, start, end, suffix_link=None):
        self.start = start
        self.end = end
        self.children = {}
        self.suffix_link = suffix_link


class SuffixTree:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.nodes = []
        self.text = s
        self.root = self._create_node(-1, -1)
        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0
        self.remainder = 0
        self.pos = -1
        self.build()

    def _create_node(self, start, end):
        node = SuffixNode(start, end)
        self.nodes.append(node)
        return node

    def _edge_length(self, node):
        return min(node.end, self.pos + 1) - node.start

    def build(self):
        for i in range(self.n):
            self._extend(i)

    def _walk_down(self, curr_node):
        length = self._edge_length(curr_node)
        if self.active_length >= length:
            self.active_edge += length
            self.active_length -= length
            self.active_node = curr_node
            return True
        return False

    def _extend(self, idx):
        self.pos = idx
        self.remainder += 1
        last_new_node = None
        while self.remainder > 0:
            if self.active_length == 0:
                self.active_edge = self.pos
            if self.text[self.active_edge] not in self.active_node.children:
                leaf = self._create_node(self.pos, float("inf"))
                self.active_node.children[self.text[self.active_edge]] = leaf
                if last_new_node:
                    last_new_node.suffix_link = self.active_node
                last_new_node = None
            else:
                nxt = self.active_node.children[self.text[self.active_edge]]
                if self._walk_down(nxt):
                    continue
                if self.text[nxt.start + self.active_length] == self.text[self.pos]:
                    if last_new_node and self.active_node != self.root:
                        last_new_node.suffix_link = self.active_node
                    self.active_length += 1
                    break
                split = self._create_node(nxt.start, nxt.start + self.active_length)
                self.active_node.children[self.text[self.active_edge]] = split
                leaf = self._create_node(self.pos, float("inf"))
                split.children[self.text[self.pos]] = leaf
                nxt.start += self.active_length
                split.children[self.text[nxt.start]] = nxt
                if last_new_node:
                    last_new_node.suffix_link = split
                last_new_node = split
            self.remainder -= 1
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = self.pos - self.remainder + 1
            else:
                self.active_node = (
                    self.active_node.suffix_link
                    if self.active_node.suffix_link
                    else self.root
                )

    def _dfs_search(self, node, idx, substring):
        if idx == len(substring):
            return True
        if substring[idx] in node.children:
            nxt = node.children[substring[idx]]
            length = min(nxt.end, self.pos + 1) - nxt.start
            edge_sub = self.text[nxt.start : nxt.start + length]
            i = 0
            while i < len(edge_sub) and idx < len(substring):
                if edge_sub[i] != substring[idx]:
                    return False
                i += 1
                idx += 1
            if i < len(edge_sub):
                return idx == len(substring)
            return self._dfs_search(nxt, idx, substring)
        return False

    def search(self, substring):
        return self._dfs_search(self.root, 0, substring)
