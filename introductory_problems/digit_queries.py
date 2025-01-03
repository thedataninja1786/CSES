import sys

data = sys.stdin.read()

def digit_queries(data):
    # find the block that the query falls into
    # block = 9*10**(k-1)*k starting with k=1
    res = []
    for q in data.splitlines()[1:]:
        q = int(q)
        k = 1 # number of digits in the current block
        start = 1 # starting digit of the current block

        while True:
            block = 9*(10**(k-1))*k
            if q <= block:
                break
            q -= block # digits in block
            k += 1 # move on to the next block of digits
            start *= 10 # new starting digit of new block

        # locate the exact number 
        num = start + (q-1) // k
        idx = (q - 1) % k
        res.append(str(num)[idx])
    
    return "\n".join(res) 

print(digit_queries(data))