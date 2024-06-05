class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0

        total_duration = 0

        for i in range(len(timeSeries) - 1):
            diff = timeSeries[i+1] - timeSeries[i]
            total_duration += min(diff, duration)

        total_duration += duration

        return total_duration
