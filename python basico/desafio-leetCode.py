class Solution(object):
    def twoSum(self, nums, target):   
        for i in range(len(nums)):
            for x in range(len(nums)):
                if i == x:
                    continue
                if nums[i] + nums[x] == target:
                    return [i, x]  
                


    print(twoSum(0,[3,2,3], 6))