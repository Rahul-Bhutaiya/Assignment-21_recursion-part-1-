#Write a recursive python function to print cubes of first N natural numbers

def cubes(n):
    if n>0:
        cubes(n-1)
        print(n**3)

n_val=int(input('Enter N Value : '))
cubes(n_val)