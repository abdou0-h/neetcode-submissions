class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        
        for digit in digits:
            res = res * 10 + digit 
        res += 1
        
        for i in range(len(digits) - 1, -1, -1):
            val = res % 10
            digits[i] = val
            res //= 10
            
        if res > 0:
            digits.insert(0, res)
            
        return digits