'''
Valid Palindrome

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_p=0
        right_p=len(s)-1
        while left_p<right_p:
            while not s[left_p].isalnum() and left_p<right_p:
                left_p+=1
            while not s[right_p].isalnum() and left_p<right_p:
                right_p-=1
            if s[left_p].lower()!=s[right_p].lower():
                return False
            left_p+=1
            right_p-=1
        return True

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
