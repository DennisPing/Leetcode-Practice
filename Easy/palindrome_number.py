# 9. Palindrome Number

# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Reverse an integer by using math instead.
        """
        if x >= 2**31-1 or x < 0:
            return False

        num = x
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        if reversed_num >= 2**31-1:
            return False
        
        return x == reversed_num

    def isPalindrome2(self, x: int) -> bool:
        """
        Palindrome by converting to string and using slices.
        """
        return False if x < 0 else x == int(str(x)[::-1])
        
solution = Solution()
print(solution.isPalindrome(-121))