# ABC is a right triangle, 90° at B.
# Therefore, ABC = 90°.
# Point M is the midpoint of hypotenuse AC.
# You are given the lengths AB and BC.
# Your task is to find MBC (angle, as shown in the figure) in degrees.

# Sample Input :
# 10
# 10

# Sample Output :
# 45°

import math
a = int(input().strip())
b = int(input().strip())

angle = str(round(math.degrees(math.atan(a/b))))
print(angle + chr(176))