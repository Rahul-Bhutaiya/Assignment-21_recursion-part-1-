#Write a recursive python function to print first N even natural numbers.

#METHOD : 1 [USING RECURSION ONLY]
def even(n):
    if n>0:
        even(n-1)
        print(n*2,end=' ')

#METHOD : 2 [USING RECURSION + LAMBDA]
even2=lambda n:print(2) if n==1 else print(n*2,even2(n-1))

#METHOD : 3 [USING ONLY LAMBDA]
even3=lambda n:[print(x*2,end=' ')for x in range(1,n+1)]

n_val=int(input('Enter N Value : '))
even3(n_val)
