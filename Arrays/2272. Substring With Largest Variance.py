'''
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters
'''
class Solution:
    def largestVariance(self, s: str) -> int:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1

        permutations = itertools.permutations(chars, 2)
        count = 0
        for a, b in permutations:
            count = max(self.kadene(a, b, s, chars), count)
        return count

    def kadene(self, a, b, s, chars):
        count = 0
        max_local = 0
        is_a = False
        is_b = False

        val_a = chars[a]
        val_b = chars[b]
        for c in s:			
            if c != a and c != b:
                continue

            if max_local < 0 and val_a != 0 and val_b != 0:
                max_local = 0
                is_a = False
                is_b = False

            if c == a:
                max_local += 1
                val_a -= 1
                is_a = True
						
            if c == b:
                max_local -= 1
                val_b -=1
                is_b = True
            
            if is_a and is_b:
                count = max(count, max_local)
        return count
