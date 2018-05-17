/*
Author: Damian Cruz
source: CodeFight (https://codefights.com)
problem name: Arcade>TheCore>Intro Gates>LateRide
problem url:https://codefights.com/arcade/code-arcade/intro-gates/aiKck9MwwAKyF8D4L
*/


def lateRide(n):
 answer=0
 numero=str(int(n/60))+str(n%60)  
 for i in numero:
  answer+=int(i)
 return answer
