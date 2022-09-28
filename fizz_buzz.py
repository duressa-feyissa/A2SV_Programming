class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        tmp = list()
        for i in range(1, n+1):
            if i % 15 == 0:
                tmp.append("FizzBuzz")
            elif i % 5 == 0:
                tmp.append("Buzz")
            elif i % 3 == 0:
                tmp.append("Fizz")
            else:
                tmp.append(str(i))
        return tmp
