#Write a recursive python function to print first N natural numbers.

def fnatural(n):
    if n>0:
        fnatural(n-1)
        print(n)

n_value=int(input('Enter N Value : '))
fnatural(n_value)