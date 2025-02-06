with open('rosalind_hamm.txt') as input_data:
    seq1, seq2 = input_data.read().strip().split()

def solution(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

print(solution(seq1, seq2))