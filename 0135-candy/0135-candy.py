class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1]*len(ratings)
        for i in range(1,len(ans)):
            if ratings[i]>ratings[i-1]:
                ans[i] = max(ans[i], ans[i-1]+1)
        for i in range(len(ans)-2, -1,-1):
            if ratings[i]>ratings[i+1]:
                ans[i] = max(ans[i], ans[i+1]+1)
        
        # print(ratings)
        # print(ans)
        return sum(ans)