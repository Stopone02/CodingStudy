def read_fasta(filename):
    sequences = {}
    current_label = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_label = line[1:]
                sequences[current_label] = ""
            elif current_label:
                sequences[current_label] += line

    return list(sequences.values())

def consensus_and_profile(dna_sequences):
    sequence_length = len(dna_sequences[0])
    profile = {'A': [0] * sequence_length, 'C': [0] * sequence_length,
               'G': [0] * sequence_length, 'T': [0] * sequence_length}

    for seq in dna_sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1

    consensus_sequence = []
    for i in range(sequence_length):
        max_nucleotide = max("ACGT", key=lambda x: profile[x][i])
        consensus_sequence.append(max_nucleotide)

    return "".join(consensus_sequence), profile

def print_results(consensus, profile):
    print(consensus)
    for nucleotide in "ACGT":
        print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")

filename = "rosalind_cons.txt"
dna_sequences = read_fasta(filename)
consensus, profile = consensus_and_profile(dna_sequences)
print_results(consensus, profile)