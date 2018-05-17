/*
Author: Damian Cruz
source: CodeFight (https://codefights.com)
problem name :Arcade>Intro>The journy begins> checkPalindrome.
problem url: https://codefights.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ
*/


def checkPalindrome(inputString):
    i=0
    j=len(inputString)-1
    while(i<=j):
        if(inputString[i]!=inputString[j]):
           return False

        i += 1
        j -= 1

    return True

