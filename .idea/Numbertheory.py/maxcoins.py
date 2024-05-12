class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i,j=0,len(piles)-1
        tot=0
        while i<j:
            tot+=piles[j-1]
            i+=1
            j-=2
        return tot
''' we pick a triplet where 3 people play , alice get highest ,bob gets lowest and i  get the middle one.
max coins i have to find out
we sort it so that the j-1 coins will be mine
and for each time i increment 1 by1 and dec j by 2 so that i get max
'''