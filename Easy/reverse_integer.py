# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

# Input: x = 120
# Output: 21

# Input: x = 0
# Output: 0

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse an integer by converting to string and using slices.
        """
        if x >= 2**31-1 or x <= -2**31:
            return 0

        numeric = str(x)
        if x >= 0:
            output = numeric[::-1]
        if x < 0:
            digits = numeric[1:]
            temp = digits[::-1]
            output = '-' + temp
        output = int(output)
        if output >= 2**31-1 or output <= -2**31:
            return 0
        return output

    def reverse2(self, x: int) -> int:
        """
        Reverse an integer by using math instead.
        """
        if x >= 2**31-1 or x <= -2**31:
            return 0
        reversed_num = 0
        negative = False
        if x < 0:
            x = abs(x)
            negative = True
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        if negative is True:
            reversed_num = -reversed_num
        if reversed_num >= 2**31-1 or reversed_num <= -2**31:
            return 0
        return reversed_num

solution = Solution()
print(solution.reverse(-1234500))