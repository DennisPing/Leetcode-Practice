class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        values = {'I':1, 
                'V':5, 
                'X':10, 
                'L':50, 
                'C':100, 
                'D':500, 
                'M':1000
                }
        
        # Go from left to right and compare current to next.
        # If the current is less than next, then subtract the value from the output.
        # Else if the current is greater than next, then add the value to the output.
        for i in range(len(s)-1):
            if values[s[i]] < values[s[i+1]]:
                output -= values[s[i]]
            else:
                output += values[s[i]]

        # The last roman numeral cannot be compared to anything.
        # So remember to add it to the final output.
        output += values[s[-1]] 
        return output

solution = Solution()
print(solution.romanToInt("MCMXCIV"))