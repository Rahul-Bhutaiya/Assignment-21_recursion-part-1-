#Write a recursive python function to print squares of first N natural numbers

def squares(n):
    if n>0:
        squares(n-1)
        print(n**2)

n_val=int(input('Enter N Value : '))
squares(n_val)