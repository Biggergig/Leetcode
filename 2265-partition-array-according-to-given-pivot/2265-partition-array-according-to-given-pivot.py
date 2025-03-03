class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot]*len(nums)
        l,r=0,len(nums)-1
        for n,rev_n in zip(nums,reversed(nums)):
            if n<pivot:
                ans[l]=n
                l+=1
            if rev_n>pivot:
                ans[r]=rev_n
                r-=1
        return ans
