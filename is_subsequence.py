 # Problem: Check if string s is a subsequence of string t.
# Strategy: Use a pointer on s and iterate through t.
# If all characters in s appear in order inside t, return True.
#Check edge cases, is S>T it cannot be TRUE
#iterate through the length of T
#if the indexs equal, point to new index in s and loop through t to find new letter that equals
#whilst doing that, check if s is on the last letter, if so, return true.
#if it ever breaks out of this loop return false

 
 def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if s == "":
            return True
        if S>T:
            return False
        j=0    
        for i in range (T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j+=1

        return False      
# Test
print(is_subsequence("abc", "ahbgdc"))  # True
print(is_subsequence("axc", "ahbgdc"))  # False