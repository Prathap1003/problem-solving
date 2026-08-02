class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice=0
        bob=0
        nums=piles.copy()
        while len(piles)>0:
            alice+=piles[0]
            del piles[0]
            bob+=piles[0]
            del piles[0]
        chance1=0
        chance2=0
        s=len(nums)//2
        while len(nums)>0:
            chance1+=nums[-1]
            del nums[-1]
            chance2+=nums[-1]
            del nums[-1]
        return alice>bob or chance1>chance2

        