from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            if radiant_queue[0] < dire_queue[0]:
                voter = radiant_queue.popleft()
                dire_queue.popleft()
                radiant_queue.append(voter + len(senate))
            else :
                voter = dire_queue.popleft()
                radiant_queue.popleft()
                dire_queue.append(voter + len(senate))

        if radiant_queue:
            return "Radiant"
        else:
            return "Dire"