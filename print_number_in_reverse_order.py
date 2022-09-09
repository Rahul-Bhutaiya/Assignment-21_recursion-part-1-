#Write a recursive python function to print a number in reverse order.

#METHOD : 1 [USING RECURSION ONLY]
def reverse(number,rev=0):
    if number>0:
        last=number%10
        rev=rev*10+last
        number//=10
        reverse(number,rev)
    else:
        print('Reverse :',rev)

#METHOD : 2 [USING RECURSION + LAMBDA]
reverse3=lambda n:'' if n==0 else str(n%10)+reverse3(n//10)

#METHOD : 3 [USING ONLY LAMBDA]
reverse2=lambda n:str(n)[::-1]

number=int(input('Enter a Number : '))
print(reverse3(number))
