class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=ans=0
        for r in range(0,len(nums)):
            if nums[r] == 0:
                k-=1
                while k<0:
                    if nums[l] == 0:
                        k+=1
                    l+=1
            ans = max(ans, r-l+1)
        return ans
                
            
        # Oh my god it was sliding window...
        # seq_starts = deque([-1]*(k+1))
        # ans = 0
        # for i,n in enumerate(nums):
        #     if n == 0:
        #         seq_starts.appendleft(i)
        #         seq_starts.pop()
        #     # print(i, seq_starts)
        #     ans = max(ans, i-seq_starts[-1])
        # return ans