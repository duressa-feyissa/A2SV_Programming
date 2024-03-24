class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        total_rabbits = 0
        for answer, count in counter.items():
            total_rabbits += ((count + answer) // (answer + 1)) * (answer + 1)
        return total_rabbits

