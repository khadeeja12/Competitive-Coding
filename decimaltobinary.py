
def decimal(num):
    stack=[]
    while num>0:
        r=num%2
        stack.append(r)
        num=num//2
    return stack[::-1]
    
num=int(input("enter a decimal number"))
l=decimal(num)
print(l)


