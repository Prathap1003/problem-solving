
def genarate(vis,digits,lst,pst):
    global count
    if len(lst)==3:
        if lst[-1]%2==0 and lst[0]!=0 and lst not in pst:
            pst.append(lst.copy())
        return 
    for i in range(len(digits)):
        if vis[i]==0:
            lst.append(digits[i])
            vis[i]=1
            genarate(vis,digits,lst,pst)
            lst.pop()
            vis[i]=0
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        vis=[0]*len(digits)
        lst=[]
        pst=[]
        genarate(vis,digits,lst,pst)
        return len(pst)
        
        
        
        
        
        