class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        my_list = []
        for index, val in enumerate(tickets):
            my_list.append([index, val])

        queue = deque(my_list)
        time = 0
    

        while True:

            current = queue.popleft()
            current[1] -= 1
            time += 1

            if current[1] == 0 and current[0] == k:
                return time
            if current[1] > 0:
                queue.append(current)


            

