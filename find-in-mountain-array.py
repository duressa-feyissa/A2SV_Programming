class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        def findCenter(left, right):
            if left > right:
                return -1
            middle = (left + right) // 2
            ll, rr = -1, -1
            if middle != 0:
                ll = mountain_arr.get(middle - 1)
            if middle != length - 1:
                rr = mountain_arr.get(middle + 1)
            cc = mountain_arr.get(middle)
            if middle == 0:
                return 1
            elif middle == length - 1:
                return length - 2
            elif cc > ll and cc > rr:
                return middle            
            elif ll < cc < rr:
                res = findCenter(middle + 1, right)
                if res != -1:
                    return res
            elif ll > cc > rr:
                res = findCenter(left, middle - 1)
                if res != -1:
                    return res
            return -1
        
        
        def findIndexDecreasingArray(left, right):
            if left > right:
                return -1
            middle = (left + right) // 2
            ll = mountain_arr.get(left)
            rr = mountain_arr.get(right)
            cc = mountain_arr.get(middle)
            if cc == target:
                return middle
            elif target > cc:
                res = findIndexDecreasingArray(left, middle - 1)
                if res != -1:
                    return res
            else:
                res = findIndexDecreasingArray(middle + 1, right)
                if res != -1:
                    return res
            return -1
        
        def findIndexIncreasingArray(left, right):
            if left > right:
                return -1
            middle = (left + right) // 2
            ll = mountain_arr.get(left)
            rr = mountain_arr.get(right)
            cc = mountain_arr.get(middle)
            if cc == target:
                return middle
            elif target < cc:
                res = findIndexIncreasingArray(left, middle - 1)
                if res != -1:
                    return res
            else:
                res = findIndexIncreasingArray(middle + 1, right)
                if res != -1:
                    return res
            return -1
            
        center = findCenter(0, length)
        value = mountain_arr.get(center)
        if value == target:
            return center
        elif target < value:
            res = findIndexIncreasingArray(0, center)
            if res != -1:
                return res
        return findIndexDecreasingArray(center, length - 1)