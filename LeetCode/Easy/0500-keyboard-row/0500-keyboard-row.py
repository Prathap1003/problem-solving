class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic={'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,'a':2,'s':2,'d':2,'f':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}
        lst=[]
        for word in words:
            min_=3
            max_=0
            for i in word:
                i=i.lower()
                min_=min(min_,dic[i])
                max_=max(max_,dic[i])
            if min_==max_:
                lst.append(word)
        return lst

        