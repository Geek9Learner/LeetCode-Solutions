class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            position=0
            if (target-nums[i]) in nums[i+1:]:
                ans.append(i)
                position =i+1+nums[i+1:].index(target-nums[i])
                ans.append(position)
                break
        return ans
        