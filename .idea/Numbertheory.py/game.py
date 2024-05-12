class Solution:
    def gcd(a, b):
        while a*b and a!=b:
          if a>b:
            a%=b
          elif b>a:
            b%=a
        return a if a>b else b
    def solve(self,a, b, n):
      while n > 0:
        if n < gcd(a, n):
            return 1
        n -= gcd(a, n)
        if n < gcd(b, n):
            return 0
        n -= gcd(b, n)
      return 1
'''Bholu and Dholu play a game. Initially each player receives one fixed positive integer that doesn't change throughout the game. Bholu receives number a and Dholu receives number b. They also have a heap of n stones. The players take turns to make a move and Bholu starts. During a move a player should take from the heap the number of stones equal to the greatest common divisor of the fixed number he has received and the number of stones left in the heap. A player loses when he cannot take the required number of stones (i. e. the heap has strictly less stones left than one needs to take).

Your task is to determine who wins the game.

Input
The only string contains space-separated integers a, b and n (1 ≤ a, b, n ≤ 100) — the fixed numbers Bholu and Dholu have received correspondingly and the initial number of stones in the pile.

Output
If Bholu wins, print "0" (without the quotes), otherwise print "1" (without the quotes).

Sample Input
3 5 9
Sample Output
0
'''