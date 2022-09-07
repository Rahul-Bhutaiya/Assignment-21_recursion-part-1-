#Write a recursive python function to print first N natural numbers in reverse order

def fnat_rev(n):
    if n>0:
        print(n,end='  ')
        fnat_rev(n-1)

n_val=int(input('Enter N Value : '))
fnat_rev(n_val)