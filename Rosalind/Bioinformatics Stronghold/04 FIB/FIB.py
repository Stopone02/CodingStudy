with open('rosalind_fib.txt') as input_data:
    n, k = map(int, input_data.read().strip().split())

def solution(n, k):
    previous, current = 1, 1
    for i in range(2, n):
        previous, current = current, current + (k * previous)
    return current

print(solution(n, k))
