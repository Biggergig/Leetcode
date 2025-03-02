class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l = 0
        out = []
        for r in range(len(nums2)):
            while l<len(nums1) and nums1[l][0] <= nums2[r][0]:
                out.append(nums1[l])
                l+=1
            if out and out[-1][0] == nums2[r][0]:
                out[-1][1]+=nums2[r][1]
            else:
                out.append(nums2[r])
        while l<len(nums1):
            out.append(nums1[l])
            l+=1
        return out