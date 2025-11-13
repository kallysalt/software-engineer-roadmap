# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams_soln1(self, strs: List[str]) -> List[List[str]]:

        # notes: 
        # only immutables are hashable: string, tiple
        # mutables are not hashable: list, hmap
        # sorted(str) will return a list
        # convert list back to string: "".join(list)
        
        # solution 1: hashmap
        # key: sorted string
        # val: anagram list

        # len(strs) = n
        # len(str) = m
        # time complexity = n * m * log(m)

        hmap = {}
        for s in strs: 
            key = ''.join(sorted(s)) 
            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]
        
        res = []
        for key in hmap:
            res.append(hmap[key])
        return res


    def groupAnagrams_soln2(self, strs: List[str]) -> List[List[str]]:

        # solution 2:
        # by the definition of an anagram
        # we only care about the frequency of each character in a string
        # we can have a list, in which element at idx = 0 represents freq of a
        
        # len(strs) = n
        # len(str) = m
        # time complexity = n * m * log(m)

        from collections import defaultdict

        hmap = defaultdict(list) # val's type
        for s in strs: 
            count = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                count[idx] += 1 
            key = tuple(count) # convert list to tuple s.t. it can act as key in dict
            hmap[key].append(s) # append returns none
            
        res = list(hmap.values()) # type(hmap.values()) = dict_values
        return res