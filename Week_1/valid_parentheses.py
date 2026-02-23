'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000


'''

class Solution:
  def isValid(self, s : string) -> bool:
    stack=[]
    closeToOpen={')' : '(' , ']' : '[' , '}' : '{'}
    for c in s:
      if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]:
          stack.pop()
        else:
          return False
      else:
        stack.append(c)
    return True if not stack else False

'''

Time & Space Complexity
  Time complexity: 
    O(n)
  Space complexity: 
    O(n)

'''
