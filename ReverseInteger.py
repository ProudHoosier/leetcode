import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = math.pow(2,31) - 1
        result = 0
        if x >= 0:
            num = str(x)
            result = int(num[::-1])
        else:
            num = str(-x)
            result = -int(num[::-1])
            
        if result < MAX_INT and result > -MAX_INT:
            return result
        else:
            return 0