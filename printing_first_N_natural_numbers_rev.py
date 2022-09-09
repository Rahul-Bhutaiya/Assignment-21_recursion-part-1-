#Write a recursive python function to print first N natural numbers in reverse order

#METHOD : 1 [USING RECURSION ONLY]
def fnat_rev(n):
    if n>0:
        print(n,end='  ')
        fnat_rev(n-1)

#METHOD : 2 [USING RECURSION + LAMBDA]        
fnat_rev2=lambda n,first=1:print(first,fnat_rev2(n,first+1)) if first<n else print(n)

#METHOD : 3 [USING ONLY LAMBDA]
fnat_rev3=lambda n:[print(x,end=' ')for x in range(n,0,-1)]

n_val=int(input('Enter N Value : '))
fnat_rev3(n_val)
