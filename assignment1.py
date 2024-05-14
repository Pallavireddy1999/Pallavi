'''1. What is the time, and space complexity of the following code: 
a = 0
b = 0
for i in range(N):
  a = a + random()

for i in range(M):
  b= b + random()

O(N + M) time, O(1) space
2.a = 0;
for i in range(N):
  for j in reversed(range(i,N)):
    a = a + i + j;
    ans:  O(N*N)
3.k = 0;
for i in range(n//2,n):
  for j in range(2,n,pow(2,j)):
        k = k + n / 2;
ans: O(nLogn)
4.What does it mean when we say that an algorithm X is asymptotically more efficient than Y? 

ans:X will always be a better choice for large inputs
5.What is the time complexity of the following code:
a = 0
i = N
while (i > 0):
  a += i
  i //= 2
ans:O(log N)
6.Which of the following best describes the useful criterion for comparing the efficiency of algorithms?
ans:Time and Memory
7.How is time complexity measured?
ans: By counting the number of primitive operations performed by the algorithm on a given input size.
8.What will be the time complexity of the following code?
for i in range(n):
  i=i*k
ans:O(logkn)

9.value = 0;
for i in range(n):
  for j in range(i):
    value=value+1
ans:n(n-1)/2
10.Algorithm A and B have a worst-case running time of O(n) and O(logn), respectively. Therefore, algorithm B always runs faster than algorithm A.
ans:False
'''