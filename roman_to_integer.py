# Problem: Convert a Roman numeral string to an integer.
# Subtractive cases (e.g., IV = 4) handled using lookahead logic.
# the if statement handles cases where there is a smaller roman before a larger one that must be combined
#It handles edge cases by using if i<n-1 so it doesnt compare to anything out of bounds, and increments by 2 as both romans used
#else statemet handles normal cases and increments by 1
def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X' :10, 'L':50, 'C': 100, 'D' : 500, 'M':1000}
        sum = 0
        n= len(s)
        i = 0

        while i<n:
            if i<n-1 and d[s[i]]< d[s[i+1]]:
                sum += d[s[i+1]] - d[s[i]]
                i+=2
            else:
                sum+= d[s[i]]
                i+=1
        return sum            

print(roman_to_int("MCMXCIV"))  # Output: 1994