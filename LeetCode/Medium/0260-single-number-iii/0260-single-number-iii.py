class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        first=0
        second=0
        answer=0
        for i in nums:
            answer=answer^i
        print(answer)
        setbit=0
        while answer:
            if answer&1>0:
                break
            setbit+=1
            answer=answer>>1
        mask=1<<setbit
        for j in nums:
            if j&mask>0:
                first^=j
            else:
                second^=j
        return [first,second]

                
        