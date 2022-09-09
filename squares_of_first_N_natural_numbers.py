#Write a recursive python function to print squares of first N natural numbers

#METHOD : 1 [USING RECURSION ONLY]
def squares(n):
    if n>0:
        squares(n-1)
        print(n**2)

#METHOD : 2 [USING RECURSION + LAMBDA]
squares2=lambda n:print(1)if n==1 else print(n**2,squares2(n-1))

#METHOD : 3 [USING ONLY LAMBDA]
squares3=lambda n:[print((x+1)**2)for x in range(n)]

n_val=int(input('Enter N Value : '))
squares3(n_val)
