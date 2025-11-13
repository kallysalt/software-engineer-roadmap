# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        # edge case: empty string

        # need a data structure that supports first in first out
        # lets try stack

        stack = []
        leftSet = set(['(', '[', '{'])

        for ch in s:
            if ch in leftSet:
                stack.append(ch)
            else:
                if ch == ')':
                    # need to make sure stack is not empty before access stack[-1]
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif ch == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif ch == ']':
                    if stack and stack[-1] == '[': 
                        stack.pop()
                    else:
                        return False
            
        return len(stack) == 0