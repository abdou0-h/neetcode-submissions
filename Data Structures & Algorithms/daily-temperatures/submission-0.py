class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        # 1. Initialize the result list with zeros
        result = [0] * n
        
        # 2. Use a list as a stack to store indices
        stack = []
        
        # 3. Loop through temperatures with index and value
        for i, temp in enumerate(temperatures):
            
            # 4. Monotonic Logic: While stack has elements 
            # and current temperature is warmer than the top of stack
            while stack and temp > temperatures[stack[-1]]:
                
                # Pop the index of the colder day
                prev_index = stack.pop()
                
                # Calculate the distance in days
                result[prev_index] = i - prev_index
            
            # 5. Push current index to wait for its warmer day
            stack.append(i)
            
        return result