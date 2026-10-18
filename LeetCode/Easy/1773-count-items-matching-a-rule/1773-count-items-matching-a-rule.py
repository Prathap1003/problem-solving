class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        answer=0
        if ruleKey=='type':
            for i,j,k in items:
                if i ==ruleValue:
                    answer+=1
            return answer
        answer=0
        if ruleKey=='color':
            for i,j,k in items:
                if j ==ruleValue:
                    answer+=1
            return answer
        answer=0
        if ruleKey=='name':
            for i,j,k in items:
                if k ==ruleValue:
                    answer+=1
            return answer
                

        