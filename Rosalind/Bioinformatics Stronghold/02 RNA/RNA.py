with open('rosalind_rna.txt') as input_data:
    dna_seq = input_data.read().strip()

def solution(dna_seq):
    rna_seq = ''
    for i in range(len(dna_seq)):
        if dna_seq[i] == 'T':
            rna_seq += 'U'
        else:
            rna_seq += dna_seq[i]
    return rna_seq

print(solution(dna_seq))
