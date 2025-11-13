# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr: # 只要当前节点存在，就继续处理
            nxt = curr.next # keep track of the next element
            curr.next = prev # reverse the link
            prev = curr # update prev
            curr = nxt # update curr
        
        return prev