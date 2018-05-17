/*
Author: Damian Cruz
source: CodeFight (https://codefights.com)
problem name: Arcade>Intro>The journy begins>CenturyFromYear
problem url: https://codefights.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
*/


def centuryFromYear(year):
    if(year/100<1):
        return(1)
    if(year%100==0):
        return(int(year/100))
    if(year%100!=0 and year>100):
        year=year/100
        year=int(year)
        year=year+1
        return(year)
