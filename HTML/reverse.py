#reverse list
a = [1,2,3,4,5,6,7,8]
for i in range(8 ,0,-1):
    print(i)
#reverse num
num = 12345
rev = 0

for i in range(len(str(num))):
    rev = rev * 10 + num % 10
    num //= 10
    print(i)

print("Reversed number:", rev)

#factorial
num=int(input("Enter Number:"))
fac=1
for i in range(num,0,-1):
    fac=fac*i
print(fac)

#fibbona
n=int(input("Enter Number:"))
fibbo=0
fibbo2=1
next=0
for i in range(n):
    print(fibbo)
    next = fibbo+fibbo2
    fibbo= fibbo2
    fibbo2=next
