with open('rosalind_dna.txt') as input_data:
    dna_seq = input_data.read().strip()

def solution(dna_seq) :
    return dna_seq.count('A'), dna_seq.count('C'), dna_seq.count('G'), dna_seq.count('T')

a, c, g, t = solution(dna_seq)
print(f"{a} {c} {g} {t}")


