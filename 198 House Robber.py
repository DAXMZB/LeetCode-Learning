# we have an input array nums as Example1 
# [1, 2, 3, 1, 9, 7] we need return the maximum amount of money  and without adjacent house
# Fist, it need iterate though each house —> amount without adjacent
# Use 2 viariable to stere the states —> prev2, prev1 (Initialize) 0, 0 represents the houses haven't been visited yet
# 0, 0 -> 0, 1  prev1, (prev2 + current)      —— switch position and amount the current max
# 2, 4 —> 4, 2 + 1 prev1, max(prev1, prev2 + current)
# we need use max to compare pre1 and prev2 + current Because if the situation current amount is (2, 4)
#   and the next would be 4, 2+1 and for now, the most important is 4 plus next like 9 or next plus 7 is
#       maximum, no matter 3 plus any, so we need max to compare each prev1, prev2 whic is max and acording
#           the max to find the maximunm , Greedy property is not enough here
class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case with boundaries
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[1]
        
        prev2, prev1 = 0, 0

        for n in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + prev1)
        return prev1

        # Time Complexity is O(N)
        #   Because we performs a linear scan through nums array
        #       the Time Complexity is proportional to the number of house

        # Space Complexity is O(1)
        #   Because we maintain 2 viriables to store the states,
        #       regardless of the input size

        