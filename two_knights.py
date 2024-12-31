n = int(input())

def valid_placements(n):
    total = ((n**2)*((n*n)-1))//2
    invalid = 4 * (n-2) * (n-1)
    return str(total-invalid) 

for i in range(1,n+1):
    print(valid_placements(i))




