        
gain=[-5,1,5,0-7]
res=0
a=0
for i in gain:
    a+=i
    res=max(res,a)
    print(res)
print(res)


''' this is recursio and every time res will have max value and updates if it gets a higher value.
'''