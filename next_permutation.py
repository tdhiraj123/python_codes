'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

note- repetation is allowed in input
'''
class Solution(object):
    def nextPermutation(self, nums):
        if(sorted(nums)==nums[::-1]):
            nums.sort()
            return nums
        i=len(nums)-1
        while i>0 and (nums[i]<=nums[i-1]):
            i=i-1
        tmp=[]
        for j in range(i,len(nums)):
            if(nums[j]>nums[i-1]):
                tmp.append(nums[j])
        nums[i-1],nums[i+nums[i:].index(min(tmp))]=min(tmp),nums[i-1]
        f=nums[i:]
        f.sort()
        for m in range(len(f)):
            nums[i+m]=f[m]
        print(nums)
        
        
        
        
