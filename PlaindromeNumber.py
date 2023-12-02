"""
Problem:
Given an integer x, return true if x is a palindrome and false otherwise
"""


class Solution:
    def isPrime(self, x:int)->bool:
        if x<0:
            return False
        rev = 0
        y = x
        while y:
            rev = rev*10 + y%10
            y //=10
        return rev == x 