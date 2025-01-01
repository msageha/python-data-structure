class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.end_of_word

    def starts_with(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True

    def delete(self, word):
        self._delete_recursive(self.root, word, 0)

    def _delete_recursive(self, current, word, index):
        if index == len(word):
            if not current.end_of_word:
                return False
            current.end_of_word = False
            return len(current.children) == 0

        ch = word[index]
        if ch not in current.children:
            return False

        node = current.children[ch]
        should_delete = self._delete_recursive(node, word, index + 1)

        if should_delete:
            del current.children[ch]
            return (not current.end_of_word) and (len(current.children) == 0)
        return False
