#Write a recursive python function to print cubes of first N natural numbers

#METHOD : 1 [USING RECURSION ONLY]
def cubes(n):
    if n>0:
        cubes(n-1)
        print(n**3)

#METHOD : 2 [USING RECURSION + LAMBDA]
cubes2=lambda n:print(1) if n==1 else print(n**3,cubes2(n-1))

#METHOD : 3 [USING ONLY LAMBDA]
cubes3=lambda n:[print(x**3,end=' ') for x in range(1,n+1)]

n_val=int(input('Enter N Value : '))
cubes3(n_val)
