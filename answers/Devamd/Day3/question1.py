n=int(input())
l=0
n1,n2=n,n
count=0
while(n1 != 0):
    lastDigit = n1 % 10
    while(n2 != 0):
        if(lastDigit == n2%10):
            count+=1
            n2 /= 10
    if(count != 1):
        return False
        n1 /= 10
    else:
        return True
