class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''this question is related to kadane's algorithms'''
        local_max=0
        global_max=-999999
        for i in range(len(nums)):
            local_max=max(local_max+nums[i],nums[i]);
            if(local_max>global_max):
                global_max=local_max;
        return global_max
    