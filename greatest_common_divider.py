#finding the greatest common divider using square tiles method
#program computes the solution using Euclidean algorithm. 

num1 = int(raw_input('Enter a number: '))
num2 = int(raw_input('Enter a number: '))

if num1 > num2:
    a = num1
    b = num2
if num2 > num1:
    a = num2
    b = num1

while (a-b) > 0:
    c = a - b

    if c > b:
        a = c
    else:
        a = b
        b = c

print 'The greatest common divider of numbers:', num1, 'and', num2, 'is', c
