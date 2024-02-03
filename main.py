

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
              dummy = ListNode(0)
              dummy.next = head
              left = dummy
              right = head 
              
              while n>0 and right:
                  right = right.next
                  n -=1
              while right:
                  left = left.next
                  right = right.next
              
              #delete 
              left.next = left.next.next
              return dummy.next 
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
                     
def main():
    #create a linkedlist
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    
    print("Original linked list:")
    print_linked_list(linked_list)

    sol =  Solution()
    
    result = sol.removeNthFromEnd(linked_list, n)
    
   
    print("\nLinked list after removal:")
    print_linked_list(result)
    
if __name__=="__main__":
    main()
    
    