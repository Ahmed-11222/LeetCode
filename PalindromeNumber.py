class Solution(object):
    def isPalindrome(self, x):
        a = x
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x /= 10
        return a == y
        