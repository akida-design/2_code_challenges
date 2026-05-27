# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next
    
# Example usage:
# Creating linked list for list1: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
# Creating linked list for list2: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))
# Merging the two sorted lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
# Printing the merged linked list
current = merged_list
while current:
    print(current.val, end=' ')
    current = current.next
# Output: 1 1 2 3 4 4