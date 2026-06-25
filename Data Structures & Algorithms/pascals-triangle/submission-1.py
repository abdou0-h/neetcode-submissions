class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        newlist = [[]]
    
        if numRows == 0:
            return []
        newlist = [[1]]
        j = 0
        
        while numRows - 1 > 0:
            newlist.append([])
            newlist[j + 1].append(1)
            
            for i in range(len(newlist[j]) - 1):
                var = newlist[j][i] + newlist[j][i + 1]
                newlist[j + 1].append(var)
                
            newlist[j + 1].append(1)
            j += 1
            numRows -= 1
            
        return newlist
