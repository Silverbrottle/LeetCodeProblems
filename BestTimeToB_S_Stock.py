def maxProfit(prices):
    minVal=max(prices)
    maxProfitVal=0
    maxVal=min(prices)
    print("minVal: ",minVal)
    print("maxVal: ",maxVal)
    for i in prices:
        if i < minVal:
            minVal=i
            maxVal=i
        if i > maxVal:
            maxVal=i
        print("minVal: ",minVal)
        print("maxVal: ",maxVal)
        maxProfitVal=max(maxProfitVal,maxVal-minVal)
        print("maxProfitVal: ",maxProfitVal)
    return maxProfitVal

maxProfit([7,6,4,3,1])