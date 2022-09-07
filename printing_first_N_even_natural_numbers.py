#Write a recursive python function to print first N even natural numbers.

def even(n):
    if n>0:
        even(n-1)
        print(n*2,end=' ')

n_val=int(input('Enter N Value : '))
even(n_val)