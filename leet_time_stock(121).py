'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.'''




'''l=list(map(int,inpt().split()))
maxp=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]>l[j+1]
           maxp=l[j]-l[j+1]'''
           


l=list(map(int,input().split(",")))
pr=0
buy=l[0]
for i in range(len(l)):
    if l[i]<buy:
        buy=l[i]
    elif l[i]-buy>pr:
         pr=l[i]-buy
print(pr)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=prices[0]
       
        max1=0
        for i in prices:
            if (min1>i):
                min1=i
            elif(i-min1)>max1:
                max1=i-min1
        return max1