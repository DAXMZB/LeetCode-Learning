class Solution:
    # [1, 9, 3, 1, 2]
    # 1 —> 3
    # 2 —> 1
    # prev2, prev1 —> prev1, prev2 + current
    # 0,    0           0, 1 max(prev1, prev2 + current)
    # 0,    1           1, 9
    # 1,    9           9, 9 
    # 9,    9           9, 10 
    # 9,    10         10, 11
    # return prev1
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[1]
            
        prev2, prev1 = 0, 0

        for n in nums:      #prev2, prev1
            prev2, prev1 = prev1, max(prev1, prev2 + n)
        return prev1

    # Time Complexity is O(n) 
    #   Since we performs a linear scan through the nums array, 
    #       the time complexity is proportional to the number of house
    # Space Complexiy is O(1) 
    #   We only maintain 2 variable (prev1, prev2) regardless of the input size, 
    #       thus achieving constant