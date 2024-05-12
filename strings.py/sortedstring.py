'''Input:
A string s of length between 1 and 10,000.

Output:
Return the smallest lexicographical order string after removing duplicates.

Example 1:
Input:

s = "bcabc"

Output:
"abc"
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
      # Write Your code here 
      unique_chars = set()
      result = []
      for char in s:
        if char not in unique_chars:
            unique_chars.add(char)
            result.append(char)
      return ''.join(sorted(result))



class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
      # Write Your code here 
      last_occurrence = {}
      stack = []
      seen = set()
  
      # Store the last occurrence of each character
      for i, char in enumerate(s):
          last_occurrence[char] = i
  
      for i, char in enumerate(s):
          if char not in seen:
              # Pop characters from stack while they are larger than the current character
              # and there is a chance of occurrence of that character later
              while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                  seen.remove(stack.pop())
              seen.add(char)
              stack.append(char)
  
      return ''.join(stack)