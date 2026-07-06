def deleteDuplicates(self, head):
    curr = head 
    prev = None
    seen = set()

    while curr:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen.add(curr.val) 
            prev = curr
        curr = curr.next
       
    return head


# - traverse the list
# - for each value, add to set
# - if this is in the set, remove it.
# - always keep track of the prev node 
# - remove the node.
# - return the head of the new linked list 

# def deleteDuplicates(self, head):
#         cur = head

#         while cur:
#             while cur.next and cur.next.val == cur.val:
#                 cur.next = cur.next.next
#             cur = cur.next
#         return head