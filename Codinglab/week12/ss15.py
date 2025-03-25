n=int(input())
s=0
i=0
while n>0:
    s=s+(n%10)+(2*i)
    i=1
    n=n//10
print(s)    