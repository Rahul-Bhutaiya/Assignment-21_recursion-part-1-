#Write a recursive python function to print first N odd natural numbers in reverse order

#METHOD : 1 [USING RECURSION ONLY]
def odd_rev(n):
    if n>0:
        print(n*2-1,end=' ')
        odd_rev(n-1)

#METHOD : 2 [USING RECURSION + LAMBDA]
odd_rev2=lambda n,first=1:print(first*2-1,odd_rev2(n,first+1))if first<n else print(n*2-1)

#METHOD : 3 [USING ONLY LAMBDA]
odd_rev3=lambda n:[print(x*2-1,end=' ') for x in range(n,0,-1)]

n_value=int(input('Enter N Value : '))
odd_rev3(n_value)
