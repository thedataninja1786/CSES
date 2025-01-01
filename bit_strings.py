n = int(input())

def generate_bit_strings(n):
    MOD = (10**9)+7
    return (2**n) % MOD

print(generate_bit_strings(n))
