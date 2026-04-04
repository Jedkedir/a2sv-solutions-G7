def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

    