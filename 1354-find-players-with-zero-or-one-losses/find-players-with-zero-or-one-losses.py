class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        lose = defaultdict(int)
        count = defaultdict(int)
        for match in matches:
            win[match[0]] += 1
            lose[match[1]] += 1
            count[match[0]] += 1
            count[match[1]] += 1
        
        return [sorted([i for i in win if win[i] == count[i]]), sorted([i for i in lose if lose[i] == 1])]