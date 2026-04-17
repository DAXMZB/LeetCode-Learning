// we given an array and , for reach the top of the floor,
// we can start with index 0 or index 1 and choopse climb 1 or 2 steps in each step to find the minimum cost
// for example if we choose 10 for 2 steps and choose 20 for 1 step to the Top position as cost 30
                            // for 1 step and choose 15 for 2 stepthe to the Top position as cost 25
// the other is choose 15 for 2 steps to the top as cost 15
// as result we shold take min cost is 15
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // 
        int prev2 = 0; // means (n-2) 
        int prev1 = 0; // means (n-1)
        // start a single loop from i = 2 because 0 and 1 is the first position, the first goal is 2
        for (int i = 2; i <= cost.length; i ++) {
            int current = Math.min(prev1 + cost[i - 1], prev2 + cost[i - 2]);
            // [15, 10, 20]  i = 2
            //  min (0 + 15,  0 + 10)
            //    min = 10 -> current
            // next i be 3
            prev2 = prev1;
            prev1 = current;

        }

        return prev1;

    }
    // Time Complexity is O(N) because we iterate through array just onece to cuompute the minimum cost for each step
    // Space Complexity is O(1) because we just use two variables to store previous states
}