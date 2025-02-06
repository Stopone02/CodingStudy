with open('rosalind_subs.txt') as input_data:
    seq1, seq2 = input_data.read().strip().split()

def solution(seq1, seq2):
    location = []
    for i in range(len(seq1) - len(seq2) + 1):
        if seq1[i:i+len(seq2)] == seq2:
            location.append(i+1)
    return location

print(" ".join(map(str, solution(seq1, seq2))))