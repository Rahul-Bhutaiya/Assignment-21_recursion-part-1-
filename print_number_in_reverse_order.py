#Write a recursive python function to print a number in reverse order.

def reverse(number,rev=0):
    if number>0:
        last=number%10
        rev=rev*10+last
        number//=10
        reverse(number,rev)
    else:
        print('Reverse :',rev)

number=int(input('Enter a Number : '))
reverse(number)