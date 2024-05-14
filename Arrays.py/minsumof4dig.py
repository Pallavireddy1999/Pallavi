def minimumSum(num: int) -> int:
        num=list(map(int,sorted(str(num),reverse=False)))
        ans=0
        pos=0
        ans1=int(str(num[0])+str(num[2]))
        ans2=int(str(num[1])+str(num[3]))
        return ans1+ans2

ans=minimumSum(4009)
print(ans)

'''
one optimization we can do is
def minimumSum(self, num: int) -> int:
        num=list(map(int,sorted(str(num),reverse=True)))
        ans=0
        pos=0
        for i in range(len(num)):
            ans+= num[i]*10**pos
            if i%2:
                pos+=1
        return ans

in this optimized code, we are trying to add digits at 0 pos as they are one's and we add the next pos multiplied by 10**pos.
we are incrementing the pos to 1 when it is odd
'''