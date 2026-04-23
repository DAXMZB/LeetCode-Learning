# [1 ][1 ][1 ][1 ][1 ][1 ][1 ] [0]
# [1 ][  ][ x]
# [1 ]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        
        return row[n - 1]

# Time Complexity is O(N * M)
    # Becaue we iterate through the (M - 1) rows and (N - 1) columns,
    #   Therefore, the total number of operation is proportional to the  product of M and N
# Spce Complexity is O(N)
    # Because we use a rolling array of size N to store only the necessary states
    #   Reduce the auxiliary space complexity to O(N)

# To reach the destination, the total stop is constant, through (m - 1) times and (n - 1 )times
# The sum is (m - 1) + (n - 1) = m + n - 2
#   we can optimize the space to O(1) as combinatorics
#       the number of unique path is the number of ways to choose m - 1 positions 
#           for down-move out of the total steps
# Total steps = (m - 1) + (n - 1) = (m + n - 2)!
# Down - move = (m - 1)!

        return math.comb(m + n - 2, m - 1)