class Solution:

    def possible(self,days,w,cap):
        
        day = 1
        ans = 0
        for i in w:
            if(i > cap): return False
            if(ans + i <= cap):
                ans = ans + i
            else:
                day =  day + 1
                ans = i
        return day <= days

    def shipWithinDays(self, w: List[int], days: int) -> int:
        #1 2 2 3 4 4
        #
       # w.sort()
        low = 0
        high = 1000000000
        ans = 1000000000
        while(low <= high):
            mid = (low + high) >> 1

            if(self.possible(days,w,mid)):
                ans = min(ans,mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans

            

        
        