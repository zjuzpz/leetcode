
public class BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices) {
        if(prices.length == 0) {return 0;}
        int maxProfit = 0;
        int lowest = prices[0];
        for(int i = 1; i < prices.length; i++) {
            maxProfit = Math.max(maxProfit, prices[i] - lowest);
            lowest = Math.min(lowest, prices[i]);
        }
        return maxProfit;
    }

}
