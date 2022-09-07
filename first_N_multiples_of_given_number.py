#Write a recursive python function to print first N multiples of a given number.

def multiples(n,number):
    if n>0:
        multiples(n-1,number)
        print(number,'*',n,'=',n*number)

num=int(input('Enter a Number : '))
n=int(input('Enter N Value : '))

multiples(n,num)