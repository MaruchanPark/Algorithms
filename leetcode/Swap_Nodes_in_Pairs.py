'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's
nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
  
Example 2:
Input: head = []
Output: []
  
Example 3:

Input: head = [1]
Output: [1]
'''

# 결과 : Runtime : 16ms, Memory Usage : 13.5MB
# 재귀적으로 풀려고 했음
# 1. example 2에 해당하는 빈 list를 거르기 위해 head를, 값이 1개만 있는 list를 거르기 위해 head.next를 확인.
# 2. 다음 값이 있으면 다음으로 넘어가서 1을 반복.
# 다른 사람들의 코드는 재귀로 풀지 않은게 많았다. 결제를 하고 답을 보고 싶다!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head and head.next:
            tmp = head.val
            head.val = head.next.val
            head.next.val = tmp
            
            if head.next.next:
                self.swapPairs(head.next.next)

        return head
