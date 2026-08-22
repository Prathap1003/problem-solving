class Solution:
    def maxNumberOfFamilies(self, n: int, res: List[List[int]]) -> int:
        cc=0
        answer=0
        second=[1]*10
        f=0
        res.sort(key=lambda x:x[0])
        ans=res[-1][0]+1
        res.append([ans,22])
        for i in range(len(res)-1):
            # if same resues are perform other resues are come then reset that mal
            hi=res[i][0]
            if hi==res[i+1][0]:
                second[res[i][1]-1]=0
            else:
                second[res[i][1]-1]=0
                f=1
            count=0
            if f==1:
                print(second)
                cc+=1
                if second[1]==second[2]==second[3]==second[4]==1:
                    second[3]=0
                    second[4]=0
                    answer+=1
                if second[3]==second[4]==second[5]==second[6]==1:
                    answer+=1
                    second[5]=0
                    second[6]=0
                if second[5]==second[6]==second[7]==second[8]==1:
                    answer+=1
                second=[1]*10
                f=0
        print(cc-1)
        return answer+(n-cc)*2



        
        