#Write a recursive python function to print first N odd natural numbers

#METHOD : 1 [USING RECURSION ONLY]
def odd(n):
    if n>0:
        odd(n-1)
        print(n*2-1,end=' ')

#METHOD : 2 [USING RECURSION + LAMBDA]
odd2=lambda n:print(1)if n==1 else print(n*2-1,odd2(n-1))

#METHOD : 3 [USING ONLY LAMBDA]
odd3=lambda n:[print((x+1)*2-1)for x in range(n)]

n_value=int(input('Enter N Value : '))
odd2(n_value)
