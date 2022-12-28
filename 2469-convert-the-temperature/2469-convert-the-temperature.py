class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result = []
        result.append(celsius + 273.15)
        result.append(celsius * 1.80 + 32.00)
        return result
        