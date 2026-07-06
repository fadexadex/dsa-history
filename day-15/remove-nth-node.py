def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:



    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    dummy = ListNode(0)
    dummy.next = head

    pos = length - n
    
    prev = dummy
    curr = head
    while pos > 0:
        prev = curr
        curr = curr.next
        pos -= 1
    
    prev.next = curr.next
    return dummy.next


# Implementation
# def remove_kth_last_node (head: ListNode, k: int) -> ListNode:
# # A dummy node to ensure there's a node before 'head' in case we
# # need to remove the head node.
# dummy = ListNode(-1)
# dummy. next = head
# trailer = leader = dummy
# # Advance 'leader k steps ahead.
# for _ in range (k):
# Leader = leader.next
# # If k is larger than the length of the linked list, no node
# # needs to be removed.
# if not leader: return head
# # Move 'leader' to the end of the linked list, keeping 'trailer'
# # k nodes behind.
# while leader.next:
# leader = leader.next
# trailer = trailer.next
# # Remove the thnode from the end.
# trailer.next = trailer.next.next
# return dummy. next