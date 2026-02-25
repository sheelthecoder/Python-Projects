number=int(input("Enter the number "))
temp=number
r=0
while number>0:
    a=number%10
    r=r*10+a
    number=number//10
if temp==r:
    print("Palindrome")
else:
    print("Not a palindrome")
