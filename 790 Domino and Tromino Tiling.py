# we have 2 shape like Domino tile and Tromino tile
# [x][x] [x][x]
#        [x]

# our task is find the Total combination through iput n
# declare the basic case 2 by 1 and 2 by 2
# F(n - 2) basic on n = 3
# [ ]
# [ ]

# F(n - 1)
# [ ][ ] with vartical and horizontal 
# [ ][ ]

# F(n) n = 3, 5 combinations
# we need to know what F(n) are
# F(n) = F(n - 1) + F(n - 2) + TopMissing(n - 1) + ButtomMissing(n - 1)
# we don't multipy F(n - 2) by 2 because we want to avoid double account, 
#   Because is already coverd by the F(n - 1) 
#       and F(n - 2) only contribution that we haven't accounted with 2 horizontal

# regardless the gree position 
# F(n - 1) set a solution with 2 combinations
# [ ][ ][x]
# [ ][ ][x]

# find the shape just with 1 Domino title with a solution with 1 combination
# F(n - 2)
# [ ][x][x]
# [ ][x][x]

# All the combination with basic F(n -1 ) and F(n - 2)
# TopMissing(n - 1)  set solution like L shpae, we found that the solution is plus the F(n - 1) shape and with Top Missing
# and Also need to know whoat TopMissing are like we found F(n) and basic on Domino and Tromino
#               TopMissing(n) = ButtomMissing(n - 1) + F(n - 2)
# [ ][x][x] ——> [ ][ ]      [ ][x]
# [ ][ ][x]     [ ][x][x]   [ ][x][x]

# Given an other L shpae we set Bottom sulution
# BottomMissing(n - 1)
#               ButtomMissing(n) = TopMissing(n - 1) + F(n - 2)
# [ ][ ][x] ——> [ ][x][x]   [ ][x][x]
# [ ][x][x]     [ ][ ]      [ ][x]

# This my logic for the state transitions, 
# i'm want make sure that does it reach an agreement ?
#   or does any consider i'm was missing 
class Solution:
    def numTilings(self, n: int) -> int:
        # base case
        MOD = 10 ** 9 + 7
        
        FF, F, T, B = 1, 1, 0, 0
        for i in range(2, i + 1):
            FF, F, T, B = F % MOD, (F + FF + T + B) % MOD, (B + FF) % MOD, (T + FF) % MOD
            
        return F
        
        # Time Complexity is O(N) 
        #   we performs a linear scan through input n times
        #       Time Complexity is depand it

        # Space Complexity is O(N)
        #   Because We store the states in dictionaries,
        # 

# Space Complexity O(1) Because we only maintain 4 constants
        

