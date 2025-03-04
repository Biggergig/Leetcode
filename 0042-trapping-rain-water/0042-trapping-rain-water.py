class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lm = height[0]
        rm = height[-1]
        ans = 0
        while l<r:
            if lm < rm:
                l+=1
                lm = max(lm, height[l])
                ans += lm - height[l]
            elif lm >= rm:
                r-=1
                rm = max(rm, height[r])
                ans += rm - height[r]
            else:
                potato

        return ans

    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        lh,rh = height[l],height[r]
        water = 0
        
        while l<=r:
            if height[l]<height[r]:
                water+=min(lh,rh)-height[l]
                l+=1
                if height[l]>lh:
                    lh=height[l]
            else:
                water+=min(lh,rh)-height[r]
                r-=1
                if height[r]>rh:
                    rh=height[r]

        return water