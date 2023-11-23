class Solution(object):
    def twoSum(self, nums, target):
       n=len(nums) #Storing the length of the string for traversal.
       for i in range(n): #This for loop iterates through the list.
            for j in range(i+1,n): #Taken a number in the list using i index,this loop gives all the adjacent elements(forms a pair of elements)
                if(nums[i]+nums[j]==target):#Checks for the target.
                 return [i,j]
