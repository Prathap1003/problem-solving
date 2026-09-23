class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        len_arr=len(arr)
        if len_arr%2==1:
            pass
        else:
            len_arr-=1
        answer=sum(arr)
        for i in range(3,len_arr+1,2):
            val=sum(arr[:i])
            answer+=val
            print(val)
            l=0
            for j in range(i,len(arr)):
                val+=arr[j]
                val-=arr[l]
                print(val)
                answer+=val
                l+=1
        return answer


        