class ProductOfNumbers:
    def __init__(self):
        self.lst=[1]
    def add(self, num: int) -> None:
        if num==0:
            self.lst=[1]
        else:
            self.lst.append(num*self.lst[-1])
    def getProduct(self, k: int) -> int:
        n=len(self.lst)
        if k>=n:
            return 0
        return self.lst[n-1]//self.lst[n-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)