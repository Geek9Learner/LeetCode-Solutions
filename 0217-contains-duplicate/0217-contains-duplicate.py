class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for item in nums:
            if item in count:
                count[item] +=1
            else:
                count[item]=1
            if count[item]>1:
                return True
        return False