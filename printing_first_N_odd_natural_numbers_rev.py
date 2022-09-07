#Write a recursive python function to print first N odd natural numbers in reverse order

def odd_rev(n):
    if n>0:
        print(n*2-1,end=' ')
        odd_rev(n-1)

n_value=int(input('Enter N Value : '))
odd_rev(n_value)