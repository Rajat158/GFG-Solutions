'''
Given two linked lists, your task is to complete the function makeUnion(), that returns the union list of two linked lists. This union list should include all the distinct elements only and it should be sorted in ascending order.

Example 1:

Input:
L1 = 9->6->4->2->3->8
L2 = 1->2->8->6->2
Output: 
1 2 3 4 6 8 9
Explaination: 
All the distinct numbers from two lists, when sorted forms the list in the output. 
Example 2:

Input:
L1 = 1->5->1->2->2->5
L2 = 4->5->6->7->1
Output: 
1 2 4 5 6 7
Explaination: 
All the distinct numbers from two lists, when sorted forms the list in the output.
Your Task:
The task is to complete the function makeUnion() which makes the union of the given two lists and returns the head of the new list.

Expected Time Complexity: O((N+M)*Log(N+M))
Expected Auxiliary Space: O(N+M)

Constraints:
1<=N,M<=104
'''
class Solution:
    def union(self, head1,head2):
        ans = set()
        while head1:
            ans.add(head1.data)
            head1 = head1.next
        while head2:
            ans.add(head2.data)
            head2 = head2.next
        dummy = Node(0)
        curr = dummy
        for data in sorted(ans):
            curr.next = Node(data)
            curr = curr.next
        return dummy.next
