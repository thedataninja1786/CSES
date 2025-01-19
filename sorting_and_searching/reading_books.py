import sys

data = sys.stdin.read().strip().split("\n")
n = int(data[0])  # Number of books
times = list(map(int, data[1].split()))

# Total time is the sum of all book times, as both readers read all books
total_time = sum(times)

# Maximum reading time for a single reader is the time required for the largest book
max_book_time = max(times)

# Total minimum time required is the greater of these two:
# 1. Sum of all book times (split between two readers).
# 2. Largest single book's reading time (cannot split this).
print(max(total_time, 2 * max_book_time))
