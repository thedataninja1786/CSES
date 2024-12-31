s = input()

def longest_repetition(s:str):
    j = -1 ; res = 1; x = s[0]

    for i in range(1,len(s)):
        if s[i] != x:
            x = s[i]
            j = i-1 
                
        res = max(res,i-j)

    return str(res)

print(longest_repetition(s))