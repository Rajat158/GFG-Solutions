'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
class Solution:
    def longestSubarray(self, nums):
        num_of_zeros_allowed = 1
        left_ptr = 0
        right_ptr = 0

        for right_ptr in range(len(nums)):
            num_of_zeros_allowed -= nums[right_ptr] == 0
            if num_of_zeros_allowed < 0:
                num_of_zeros_allowed += nums[left_ptr] == 0
                left_ptr += 1

        return right_ptr - left_ptr
