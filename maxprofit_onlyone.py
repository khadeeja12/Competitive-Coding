def find_max_profit(prices):
    
    if not prices:
        return 0  

    min_price = prices[0]  
    max_profit = 0  

   
    for i in range(1, len(prices)):
        
        profit = prices[i] - min_price
        
        max_profit = max(max_profit, profit)
       
        min_price = min(min_price, prices[i])

    return max_profit   
                


prices=input("eneter the prices for each day :")
prices=list(map(int,prices.split()))
a=find_max_profit(prices)
print(a)