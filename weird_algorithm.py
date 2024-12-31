n = int(input())

def weird(n):
    ls = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n*3)+1 
        ls.append(n)
    return " ".join([str(x) for x in ls])

print(weird(n))