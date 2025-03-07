class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth(l1, l2, k):
            if len(l1)>len(l2):
                l1,l2=l2,l1
            if not l1 or not l2:
                return (l1+l2)[k]
            m1 = len(l1)//2
            m2 = len(l2)//2
            if k > m1 + m2:
                if l1[m1]<l2[m2]:
                    return find_kth(l1[m1+1:], l2, k-m1-1)
                else:
                    return find_kth(l1, l2[m2+1:], k-m2-1)
            else:
                if l1[m1]>l2[m2]:
                    return find_kth(l1[:m1], l2, k)
                else:
                    return find_kth(l1, l2[:m2], k)
                    
        target = len(nums1)+len(nums2)
        if target%2 == 0:
            return (find_kth(nums1,nums2, target//2)+find_kth(nums1,nums2, target//2 - 1))/2
        else:
            return find_kth(nums1,nums2, target//2)