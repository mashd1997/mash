ddef sum_array(array):

    if type(array) == int:
        return array

    sum = 0
    for i in array:
        if type(i) == list:
            sum = sum+sum_array(i)
        else:
            sum = sum+i
    return sum

def fibonacci(n):
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):
    reversal = word[::-1]
    return reversal
    
