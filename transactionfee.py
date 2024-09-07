def find_max_profit(prices,trans):
    max_pro=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            max_pro+=prices[i]-prices[i-1]-trans
            i+=i
    return max_pro



prices=input("enter the prices :")
tran=int(input("enter the trasaction fee :"))
prices=list(map(int,prices.split()))
f=find_max_profit(prices,tran)
print(f)
