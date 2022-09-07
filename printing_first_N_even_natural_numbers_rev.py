#Write a recursive python function to print first N even natural numbers in reverse order.

def even_rev(n):
    if n>0:
        print(n*2,end=' ')
        even_rev(n-1)

n_val=int(input('Enter N Value : '))
even_rev(n_val)