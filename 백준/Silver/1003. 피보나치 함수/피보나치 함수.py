import sys 
input = sys.stdin.readline 

fibonacci_counts = [(1, 0), (0, 1)]

for i in range(2, 41):
    prev_count_0, prev_count_1 = fibonacci_counts[i - 1]
    curr_count_0, curr_count_1 = fibonacci_counts[i - 2]
    count_0 = curr_count_0 + prev_count_0
    count_1 = curr_count_1 + prev_count_1
    fibonacci_counts.append((count_0, count_1))

T = int(input())

for i in range(T):
    x = int(input())
    count_0, count_1 = fibonacci_counts[x]
    print(count_0, count_1)
