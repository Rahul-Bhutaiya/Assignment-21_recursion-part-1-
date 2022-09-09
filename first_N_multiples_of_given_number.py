#Write a recursive python function to print first N multiples of a given number.

#METHOD : 1 [USING RECURSION ONLY]
def multiples(n,number):
    if n>0:
        multiples(n-1,number)
        print(number,'*',n,'=',n*number)

#METHOD : 2 [USING RECURSION + LAMBDA]
multiples2=lambda n,number:print(number,'*',n,':',number)if n==1 else print(number,'*',n,':',number*n,multiples2(n-1,number))

#METHOD : 3 [USING ONLY LAMBDA]
multiples3=lambda n,number:[print(number,'*',x,':',number*x)for x in range(1,n+1)]

num=int(input('Enter a Number : '))
n=int(input('Enter N Value : '))

multiples3(n,num)
