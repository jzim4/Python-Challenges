# Suppose p is the perimeter of a right triangle with integral length sides, {a,b,c}.
# There are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximized?
import math

perimeter = 0
solutions = []
for side1 in range(1,999):
    for side2 in range(1,999):
        side3 = math.sqrt((side1*side1) + (side2*side2))
        if side1+side2+side3 < 1000 and math.ceil(side3) == side3:
            solutions.append(side3+side2+side1)

fullList=solutions
set(solutions)
sumsaver=[]

for x in solutions:
    counter=0
    for y in fullList:
        if x==y:
            counter+=1
    sumsaver.append([counter,x])
print("The number of solutions is maximized when p = " + str(max(sumsaver)[1]))
