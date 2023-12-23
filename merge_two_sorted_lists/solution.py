# def mergeTwoLists(l1, l2):
#     merged = []
    
#     while l1 and l2:
#         if l1[0] < l2[0]:
#             merged.append(l1.pop(0))
#         else:
#             merged.append(l2.pop(0))
    
#     merged.extend(l1 or l2)
    
#     return merged

# # Example usage
# list1 = [1, 2, 4]
# list2 = [1, 3, 4, 5]
# print(mergeTwoLists(list1, list2))  # Expected to return [1, 1, 2, 3, 4, 4, 5]


##### ListNode solution #####

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Link the remaining part of l1 or l2
    if l1 or l2:
        tail.next = l1 if l1 else l2
    
    return dummy.next

# Example usage:
# You would need to create ListNode objects for l1 and l2 before calling this function.

