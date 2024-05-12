from collections import math
def simplifiedFractions(n: int) ->[str]:
        lst=[]
        for x in range(1,n+1):
            for y in range(1,n+1):
                if x<y and math.gcd(x,y)==1:
                   lst.append(str(x)+"/"+str(y)) 
        return lst

ans=simplifiedFractions(2)
print(ans)


'''to get fractions of a number between 0 and 1 ,x<y and the gcd should be 1 which means it can't be simplified further
we used math func to find gcd

'''