/*
Author: Damian Cruz
source: CodeFight (https://codefights.com)
problem name: Arcade>TheCore>Intro Gates>PhoneCall
problem url: https://codefights.com/arcade/code-arcade/intro-gates/mZAucMXhNMmT7JWta
*/


def phoneCall(min1, min2_10, min11, s):
    minutes=0
    resta(min1,s,1,minutes)
    resta(min2_10,s,9,minutes)
    resta(min11,s,90,minutes)



def resta(cost,s,rang,minutes):
    for i in range(rang):
        if s-cost<0:
            return minutes
        s-=cost
        minutes+=1
