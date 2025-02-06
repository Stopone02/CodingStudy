with open("rosalind_iprb.txt", "r") as file:
    k, m, n = map(int, file.readline().split())

def solution(k, m, n):
    T = k + m + n
    prob = 0
    prob += (k / T) * ((k - 1) / (T - 1)) * 1.0
    prob += (k / T) * (m / (T - 1)) * 1.0
    prob += (m / T) * (k / (T - 1)) * 1.0
    prob += (k / T) * (n / (T - 1)) * 1.0
    prob += (n / T) * (k / (T - 1)) * 1.0
    prob += (m / T) * ((m - 1) / (T - 1)) * 0.75
    prob += (m / T) * (n / (T - 1)) * 0.5
    prob += (n / T) * (m / (T - 1)) * 0.5
    return round(prob, 5)

print(solution(k, m, n))
