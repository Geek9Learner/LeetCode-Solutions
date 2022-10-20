class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0 # buying day of stock
        right=1 # because user will buy first then only sell
        max_profit=0
        while(right<len(prices)):
            current_profit=prices[right]-prices[left]
            if(prices[left]<prices[right]):
                max_profit=max(current_profit,max_profit)
            else:
                left=right
            right +=1
        return max_profit
    
        """below code have TLE O(n^2) now think differently
        local_max=-1
        global_max=0
        for i in range(len(prices)-1):
            global_max=max(prices[i+1:])-prices[i]
            local_max=max(global_max,local_max)
        if local_max<=0:
            return 0
        return local_max"""
        
        
        