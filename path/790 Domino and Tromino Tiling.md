# we need use 2 tile of Domino tile and Tromino tile to combination the all possible ways
class Solution:
    # base case
    # n = 1 
    # [ ]
    # [ ]

    # n = 2
    # [ ][ ] [ ][ ]
    # [ ][ ] [ ][ ]
    
    # n = 3
    # F (n - 1)
    # [ ][ ][x] [ ][ ][x] case
    # [ ][ ][x] [ ][ ][x]

    # F (n - 2)
    # [ ][x][x]           case
    # [ ][x][x]

    # TopMissing (n - 1)                TopMissing (n) = BottomMissing (n - 1) + F (n - 2)
    # [ ][x][x]           case  —————>  [ ][ ]          [ ][x]
    # [ ][ ][x]                         [ ][x][x]       [ ][x][x]

    # BottomMissing (n - 1)             BottomMissing(n) = TopMissing (n -1) + F (n - 2)
    # [ ][ ][x]           case  —————>  [ ][x][x]       [ ][x][x]
    # [ ][x][x]                         [ ][ ]          [ ][x]

    # F (n) = F (n - 1) + F (n - 2) + TopMissing (n - 1) + BottomMissing (n - 1)
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        F, T, B = {0: 1, 1: 1}, {1: 0},{1: 0}
        for i in range(2, n + 1):
            F[i] = (F[i - 1] + F[i - 2] + T[i - 1] + B[i - 1]) % MOD
            T[i] = (B[i - 1] + F[i - 2]) % MOD
            B[i] = (T[i - 1] + F[i - 2]) % MOD
        return F[n] 

    # Time Complexity O(N)
    #              Because we just iterate once through the loop 2 to N

    # Space Complexity O(N)

        

