from itertools import accumulate
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        def getPre(heights):
            pre = [0]*len(heights) # let pre be the sum from this point to the left
            S = [] # Every index in this stack's value is monotonically increasing,
                # If the element is not in the stack, it is larger than every 
                # value seen before and has been clamped to H[S[-1]]
    
            for i,h in enumerate(heights):
                while S and heights[S[-1]] > h:
                    S.pop()
                # keep monotonic property
                if S:
                    j = S[-1] # this is the ind of first smaller value than H[i]
                    pre[i]+=pre[j] # add whatever was possible from there
                    # every value from j till i is greater than h, so add rectangle
                    pre[i]+=(i-j)*h
                else:
                    pre[i]+=(i+1)*h # every value before this is larger so we can just add rectangle
                S.append(i)
            return pre
        pre = getPre(heights[:])
        post = getPre(heights[::-1])[::-1] # reverse list, then reverse output

        # left sum from this peak, right sum from this peak, and remove double count
        return max(pre[i]+post[i]-heights[i] for i in range(len(heights)))
    
    
        # ans = 0
        # for i in range(len(heights)):
        #     ans = max(
        #         ans,
        #         sum(accumulate(heights[i::-1], min)) \
        #         + sum(accumulate(heights[i:], min)) \
        #         - heights[i]
        #     )
        # return ans