class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
        if month==1:
            month=13
            year-=1
        elif month==2:
            month=14
            year-=1
        k=year%100 #last two digits of year 
        j=year//100 # first two digits of year
        h=(day+(13*(month+1))//5+k+k//4+j//4+5*j)%7
        return days[h]
