class Solution(object):
    def reverseList(self, head):
            curr = head.next
            head.next = None 

            while curr:
              temp = curr.next
              curr.next = head
              head = curr 
              curr = temp
            return head
                