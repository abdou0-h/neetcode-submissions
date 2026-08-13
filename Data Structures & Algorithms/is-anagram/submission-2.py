import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash_table = {char: 0 for char in string.ascii_lowercase}

        for char in s:
            hash_table[char] += 1
        
        for val in t:
            hash_table[val] -= 1
            if hash_table[val] == -1:
                return False
            
        return True