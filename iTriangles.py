# We will define Neighborly Isosceles Triangles as isosceles triangles whose
# third side differs from the other two by 1.  All sides and area are integers.
# For example, the triangle of sides 5-5-6 is neighborly and has an area of
# 12.  Find the sum of the perimeters of all neighborly isosceles triangles
# with integer side lengths and whose perimeter do not exceed one million.
import math
def isWholeArea(side1, base):
    height = math.sqrt(side1*side1 - base*base*.25)
    if math.ceil(height*base/2)==height*base/2:
        return True
    else:
        return False

answer =[]
for side in range(2,333336):
    for change in range(-1,2,2):
        if 2*side > side+change:
            triangle = side*3 + change
            if triangle < 1000000 and isWholeArea(side, side+change):
                answer.append(triangle)
                print([side, side, side+change, triangle])

print('The sum of the perimeters is ' + str(sum(answer)))
