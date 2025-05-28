 
# Problem: Return an array where each element is the product of all other elements in the array, without using division.
# Strategy: Use prefix and suffix arrays to track product before and after each index.
# Suffix works right to left and skips last index (first going right to left in loop as there is nothing to the right)
# Prefix works same way but left to right
# Time: O(n), Space: O(n)
 def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1]*n
        suffix = [1]*n
        result = [0]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2,-1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            result[i] = suffix[i]*prefix[i]
        return result        
print(product_except_self([1, 2, 3, 4]))        # Output: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))   # Output: [0, 0, 9, 0, 0]        