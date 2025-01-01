class SinglyListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, value):
        new_node = SinglyListNode(value)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, value):
        new_node = SinglyListNode(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def pop_front(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def pop_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        value = second_last.next.value
        second_last.next = None
        return value

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        prev = self.head
        while prev.next:
            if prev.next.value == value:
                prev.next = prev.next.next
                return True
            prev = prev.next
        return False

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result
