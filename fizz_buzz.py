class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        hold = list()
        for i in range(1, n+1):
            if i % 15 == 0:
                hold.append("FizzBuzz")
            elif i % 5 == 0:
                hold.append("Buzz")
            elif i % 3 == 0:
                hold.append("Fizz")
            else:
                hold.append(str(i))
        return hold
