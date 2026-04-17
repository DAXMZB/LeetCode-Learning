class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();

        backTrack(result, new ArrayList<>(), k, n, 1);

        return result;

    }

    private static void backTrack(List<List<Integer>> result, List<Integer> current, int k, int target, int start) {
        if (current.size() == k) {
            if (target == 0) {
                result.add(new ArrayList<>(current));
            }
            return;
        }

        int remainCount = k - current.size();
        for (int i = start; i <= 9; i ++) {
            
            // pruning optimization
            // arithmetic sequence
            int minSum = (i + (i + (remainCount - 1))) * remainCount / 2;
            if (minSum > target) {
                break;
            }

            current.add(i);
            backTrack(result, current, k, target - i, i + 1);

            current.remove(current.size() - 1);

        }
    }
    // Time Complexity is Big O of 9 choose k,
    //  Because we use 9 limity number and only take k combinations

    // Space Complexity is Big O of k 
    //  Because is due to recursion depth and current size, both are limity by value of  k
}