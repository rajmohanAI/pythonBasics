class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                result += roman_map[s[i]]
                return result
            if roman_map[s[i]] >= roman_map[s[i + 1]]:
                result += roman_map[s[i]]
            else:
                result += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 1
            i += 1
        return result

# Creating an instance of the class
solution = Solution()

# Taking user input
roman_numeral = input("Enter a Roman numeral: ").upper()

# Converting the Roman numeral to an integer
result = solution.romanToInt(roman_numeral)

# Displaying the result
print(f"The integer value of {roman_numeral} is {result}.")
