#Write a recursive python function to print first N even natural numbers in reverse order.

#METHOD : 1 [USING RECURSION ONLY]
def even_rev(n):
    if n>0:
        print(n*2,end=' ')
        even_rev(n-1)

#METHOD : 2 [USING ONLY LAMBDA]
even_rev2=lambda n:[print(x*2,end=' ') for x in range(n,0,-1)]

n_val=int(input('Enter N Value : '))
even_rev2(n_val)
