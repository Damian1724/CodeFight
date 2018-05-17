/*
Author: Damian Cruz
source: CodeFight (https://codefights.com)
problem name: Arcade>TheCore>Intro Gates>MaxMultiple
problem url: https://codefights.com/arcade/code-arcade/intro-gates/HEsmEacHr2s9wahjr
*/


def maxMultiple(divisor, bound):
    for i in range(bound):
        if bound%divisor==0:
            return bound
        bound-=1
