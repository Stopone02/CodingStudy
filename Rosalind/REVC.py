with open('/Users/jiwon/Downloads/rosalind_revc.txt') as input_data:
    dna_seq = input_data.read().strip()

def solution(dna_seq):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ''
    for i in reversed(dna_seq):
        complement += complement_map[i]
    return complement

print(solution(dna_seq))