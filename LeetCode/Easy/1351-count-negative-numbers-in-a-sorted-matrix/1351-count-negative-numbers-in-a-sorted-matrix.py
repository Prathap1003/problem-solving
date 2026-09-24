class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count=0
        for row in grid:
            l=0
            r=len(row)-1
            if row[l]<0 and row[r]<0:
                count+=len(row)
                continue
            while l<=r:
                mid=(l+r)//2
                if row[mid]<0:
                    r=mid-1
                else:
                    l=mid+1
            count+=(len(row)-l)
        return count
        