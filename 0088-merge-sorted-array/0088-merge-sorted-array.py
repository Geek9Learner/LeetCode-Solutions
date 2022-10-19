class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp=[]
        i=0;j=0
        while(i<m and j<n):
            if(nums1[i]<=nums2[j]):
                temp.append(nums1[i])
                i=i+1
                continue
            else:
                temp.append(nums2[j])
                j=j+1
        while(i<m):
            temp.append(nums1[i])
            i=i+1
        while(j<n):
            temp.append(nums2[j])
            j=j+1
        for i in range(len(temp)):
            nums1[i]=temp[i]