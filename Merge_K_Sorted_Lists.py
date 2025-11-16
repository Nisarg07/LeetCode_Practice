import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        min_heap = []
        heapq.heapify(min_heap)
        unique_id = 0
        ans = ListNode()
        head = ans

        for node in lists:
            if node:
                heapq.heappush(min_heap,(node.val,unique_id,node))
                unique_id += 1
        
        while min_heap:
            pop_node = heapq.heappop(min_heap)
            ans.next = pop_node[2]
            ans = ans.next
            if pop_node[2] and pop_node[2].next:
                unique_id += 1
                heapq.heappush(min_heap,(pop_node[2].next.val,unique_id,pop_node[2].next))

        return head.next