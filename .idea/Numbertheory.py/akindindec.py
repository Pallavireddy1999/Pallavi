from collections import Counter
def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def getgcd(a,b):
            while a * b and a!=b:
                if a>b:
                    a%=b
                elif b>a:
                    b%=a
            return a if a >b else b
                    
        counter=collections.Counter(deck)
        cur_gcd=0
        for count in counter.values():
            cur_gcd= getgcd(cur_gcd,count)
        return cur_gcd >1
'''#leetcode 914
we created a dict with 2 values which has the item and the num of items in it using the Counter() functi
we took values which is the second in dict and finding the gcd by using a fun which includes euclidean algorithm
written in gcd 

'''


