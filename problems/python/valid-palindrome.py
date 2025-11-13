class Solution:
    # https://leetcode.com/problems/valid-palindrome/description/
    
    def isPalindrome(self, s: str) -> bool:

        # first convert all letters to lowercase
        # then turn s into a list for easy access to each character
        # two pointer: l, r
        # if not alpha -> skip

        arr = list(s.lower())
        l, r = 0, len(arr) - 1

        while l < r: # TODO
            if not arr[l].isalpha() and not arr[l].isdigit():
                l += 1
                continue
            if not arr[r].isalpha() and not arr[r].isdigit():
                r -= 1
                continue
            if not arr[l] == arr[r]:
                return False
            l += 1
            r -= 1
        
        return True


