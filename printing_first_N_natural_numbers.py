#Write a recursive python function to print first N natural numbers.

#METHOD : 1 [USING RECURSION ONLY]
def fnatural(n):
    if n>0:
        fnatural(n-1)
        print(n)

#METHOD : 2 [USING RECURSION + LAMBDA]        
fnatural2=lambda n:print(1) if n==1 else print(n,fnatural2(n-1))

#METHOD : 3 [USING ONLY LAMBDA]
fnatural3=lambda n:[print(x+1,end=' ')for x in range(n)]

n_value=int(input('Enter N Value : '))
fnatural3(n_value)
