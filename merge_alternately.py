# Problem: Merge two strings by alternating characters.
# If one is longer, append the rest at the end.
# Let first while handle if the strings are of equal length and build from there
# In first while, alternate between appending word 1 and word 2, and increment by 1
#The last 2 whiles handle the cases in which word 1 length >word 2 or vice versa
#return statements take a list with the individual character and joins them into a string

def mergeAlternately(self, word1: str, word2: str) -> str:
        A = len(word1)
        B = len(word2)
        a,b = 0,0
        word = 1
        merge = []
        while a<A and b<B:
            if word ==1:
                merge.append(word1[a])
                a+=1
                word = 2
            else:
                merge.append(word2[b])
                b+=1    
                word = 1
        while a<A:
            merge.append(word1[a])
            a+=1
        while b<B:
            merge.append(word2[b])
            b+=1
        return ''.join(merge) 

print(merge_alternately("abc", "xyz"))  # Output: "axbycz"