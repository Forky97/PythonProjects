factorial = lambda x: 'negative detect' if x<0 else x if x==1 else x*factorial(x-1)
print(factorial(5))