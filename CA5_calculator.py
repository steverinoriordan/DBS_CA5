import math
# Describe what the program does
if __name__ == '__main__':
    print "This program allows the user to perform the following calculator functions:\nAdd\nSubtract\nMultiply\nDivide\nExponent\nSquare root\nSquared\nCubed\nFactorial\nAbsolute value"
    function = raw_input("Type the function you wish you use: ")

# prompt the user to enter either one or two numbers depending on which function they choose and print the appropriate result
    if function == 'Add':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        reduce(lambda x, y: x+y, c)
        print a,"+",b,"=",reduce(lambda x, y: x+y, c)
    elif function == 'Subtract':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        reduce(lambda x, y: x-y, c)
        print a,"-",b,"=",reduce(lambda x, y: x-y, c)    
    elif function == 'Multiply':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        reduce(lambda x, y: x*y, c)
        print a,"multiplied by",b,"=",reduce(lambda x, y: x*y, c)
    elif function == 'Divide':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        reduce(lambda x, y: x/y, c)
        print a,"divided by",b,"=",reduce(lambda x, y: x/y, c)
    elif function == 'Exponent':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        reduce(lambda x, y: x**y, c)
        print a,"to the power of",b,"=",reduce(lambda x, y: x**y, c)
    elif function == 'Square root':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        map(lambda x:math.sqrt(x), c)
        print "The square roots of",a,"and",b,"are",map(lambda x:math.sqrt(x), c),"respectively"
    elif function == 'Squared':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        map(lambda x:x*x, c)
        print a,"squared and",b,"squared are",map(lambda x:x*x, c),"respectively"
    elif function == 'Cubed':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        map(lambda x:x*x*x, c)
        print a,"cubed and",b,"cubed are",map(lambda x:x*x*x, c),"respectively"
    elif function == 'Factorial':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        map(lambda x:math.factorial(x), c)
        print "The factorial of",a,"and",b,"are",map(lambda x:math.factorial(x), c),"respectively"
    elif function == 'Absolute value':
        a = float(raw_input('Enter a number: '))
        b = float(raw_input('Enter another number: '))
        c = [a,b]
        map(lambda x:abs(x), c)
        print "The absolute values of",a,"and",b,"are",map(lambda x:abs(x), c),"respectively"
    else:
        print "Not a valid function"