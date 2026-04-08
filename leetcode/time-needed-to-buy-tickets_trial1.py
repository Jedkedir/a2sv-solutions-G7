class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(tickets[i], i) for i in range(len(tickets))])
        seconds = 0
        while queue:
            ticketsNeeded, index = queue.popleft()
            seconds += 1
            if index == k and ticketsNeeded == 1:
                return seconds
            if ticketsNeeded > 1:
                queue.append((ticketsNeeded - 1, index))
        return seconds