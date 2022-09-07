#Write a recursive python function to print first N odd natural numbers

def odd(n):
    if n>0:
        odd(n-1)
        print(n*2-1,end=' ')

n_value=int(input('Enter N Value : '))
odd(n_value)