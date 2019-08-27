'''
find unique pair of sum of 3 numbers that is equal to 0

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pre=[]
        f=[]
        spr=[]
        for i in range(len(nums)-2):
            if(nums[i] not in pre):
                pre.append(nums[i])
                for j in range(i+1,len(nums)-1):
                    if(sorted([nums[i],nums[j]]) not in spr):
                        spr.append(sorted([nums[i],nums[j]]))
                        for z in range(j+1,len(nums)):
                            if((nums[i]+nums[j]+nums[z]==0) and (sorted([nums[i],nums[j],nums[z]]) not in f)):
                                f.append(sorted([nums[i],nums[j],nums[z]]))
        return(sorted(f))
            
'''
class Solution(object):
    def threeSum(self, nums):
        res = set()
        nums.sort()
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        return list(res)
                
        
