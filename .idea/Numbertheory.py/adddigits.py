def addDigits(num: int) -> int:
        if num<=9: return num
        tot=0
        while num>0:
            tot+=num%10
            num=num//10
        return addDigits(tot)

'''we are making a recursive call here on the nums:
38==> 3+8=11==> 1+1=2
we send 11 after exiting from the while loop as num to the same func addDigits
if num is a single digit,we return the same
if it is not a single digit, it goes through the loop to add those digits 
if we get a double digit agian we go through the loop


'''
