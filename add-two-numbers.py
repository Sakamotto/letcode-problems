"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class Solution():
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        result_list: ListNode = None

        current_node = l1
        current_node_l2 = l2
        carrier = 0

        while current_node != None and current_node_l2 != None:
           result = current_node.val + current_node_l2.val + carrier
           
           if result > 9:
               carrier = 1
               result = result % 10
           else:
               carrier = 0

           if(result_list == None):
               result_list = ListNode(result)
               head = result_list
           else:
               result_list.next = ListNode(result) 
               result_list = result_list.next
            
           current_node = current_node.next
           current_node_l2 = current_node_l2.next
        # end calculation

        while current_node != None:
            result = current_node.val + carrier
            
            if result > 9:
               carrier = 1
               result = result % 10
            else:
               carrier = 0

            result_list.next = ListNode(result) 
            result_list = result_list.next
            current_node = current_node.next
        #
        
        while current_node_l2 != None:
            result = current_node_l2.val + carrier
            
            if result > 9:
               carrier = 1
               result = result % 10
            else:
               carrier = 0

            result_list.next = ListNode(result) 
            result_list = result_list.next
            current_node_l2 = current_node_l2.next
        #
        if(carrier > 0):
            result_list.next = ListNode(1) 
        return head
    # end add

# end solution class
