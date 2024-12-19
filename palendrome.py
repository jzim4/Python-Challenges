#Find the largest palindrome made from the product of two 3-digit numbers.

products = []
palendromes = []

def reverse(number):
    string = str(number)
    list = []
    for i in string:
        list.append(i)
    list.reverse()
    reversestring = ''.join(list)
    reversenumber = int(reversestring)

    return reversenumber


for x in range(1001):
    for y in range(1001):
        products.append([x*y, x, y])

for i in products:
    if i[0] == reverse(i[0]):
        palendromes.append(i)

#this gives the max of the first attribute of each list, and includes
#   the whole list, which has the product and  two factors
print(max(palendromes))
