class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        l1=len(nums1)
        l2=len(nums2)
        if(l1<=l2):
            for value in nums1:
                if value in nums2:
                    ans.append(value)
                    nums2.remove(value)
        else:
            for value in nums2:
                if value in nums1:
                    ans.append(value)
                    nums1.remove(value)
        return ans
        