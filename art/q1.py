from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screenWidth, screenHeight)

from math import *

print "This is art mode!"


print screenWidth
print screenHeight

spot(0,10,20)

for i in range(10,screenWidth,20):
  for j in range(10,screenHeight,20):
    circle(i,j,10)

def handle_mousemove(x,y):
  if hypot((x+10)%20,(y+10)%20)<=20:
    spot((x//20)*20+10,(y//20)*20+10,10)