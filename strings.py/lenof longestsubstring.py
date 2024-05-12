
# to find the length of longest substring in a given string , we are going thruogh the chars and updating the index if it is repeated
# if char is not present in list we add into it
# if char is present already and index of char lies i the range of start from the substring,that means there is a collision
#as there is collision,we start a new substring after the collision element 
#cur len would be i- index of the repeated string.
#the index of the repeated char is updated and new substring continues until we find a repeated char

def lengthOfLongestSubstring(s: str) -> int:
    sub={}
    cur_sub_start=0
    cur_len=0
    longest=0
    for i, char in enumerate(s):
        if char in sub and sub[char]>=cur_sub_start:
            print(sub[char])
            cur_sub_start = sub[char]+1
            cur_len=i-sub[char]
            sub[char]=i
        else:
            sub[char]=i
            cur_len+=1
            if cur_len>longest:
                longest=cur_len
    return longest

ans = lengthOfLongestSubstring("abcabcbb")
print(ans)
