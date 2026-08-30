class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        first_window=sum(arr[:k])
        if first_window/k>=threshold:
            count+=1
        for i in range(1,len(arr)-k+1):
            first_window-=arr[i-1]
            first_window+=arr[i+k-1]
            if first_window/k>=threshold:
                count+=1
        return count
            

        