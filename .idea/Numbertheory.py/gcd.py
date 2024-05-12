def findGCD(nums:[int]) -> int:
        a=min(nums)
        b=max(nums)
        result=[]
        i=1
        while(b>=i):
            if(a % i ==0 and b % i ==0):
                result.append(i)
            i+=1
        return result[-1]
ans=findGCD([2,5,6,9,10])
print(ans)



'''Starting i with 1 so it does not give zero modulo error 
 result will have more values as 2 nums will have more divisors and we need to get the highest which will be stored in the last of result
 while loop is better to use for runtime error
 another logic which is euclidean to find gcd
 it repeatedly reduces the value until it becomes the gcd
 
 while a * b and a!=b:
                if a>b:
                    a%=b
                elif b>a:
                    b%=a
            return a if a >b else b

'''
