## Problem: Return the number in nums closest to 0
# If 2 numbers are equally close return the positive one
# Strategy: loop through nums and get the smallest absolute value by comparing to closest
#If there is a case where there is a - and + value, check if both those values are in the array, return the larger one

def findClosestNumber(self, nums):
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return(closest)         
print(find_closest_to_zero([1, -1, 2, -2]))            