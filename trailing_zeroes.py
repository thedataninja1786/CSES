
n = int(input())

def trailing_zeroes(n):
    """ Legendre's formula 
        Trailing zeroes are caused by 10, which is the product of 
        2 and 5. Devide by either factor until the denominator 5**p > n
    """
    res = 0
    i = 1
    while True:
        if n >= (5 ** i):
            res += n // 5**i
        else:
            return res
        
        i += 1
    

print(trailing_zeroes(n))
