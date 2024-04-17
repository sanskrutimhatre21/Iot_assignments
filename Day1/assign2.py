
num = int(input("Enter the Number : "))

print("The face value : {}".format(num))
d= num/1000
rd=d
d=d*1000
num=num%1000


c= num/100
rc=c
c=c*100
num=num%100

b= num/10
rb=b
b=b*10
num=num%10

a= num
ra=num

print(f"Place value of Number : {d,c,b,a}")

print(f"REverse form of number : {ra,rb,rc,rd}")