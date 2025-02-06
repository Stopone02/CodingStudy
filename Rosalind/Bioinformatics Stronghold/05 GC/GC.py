with open('rosalind_gc.txt') as input_data:
    sequences = {}
    current_label = ""
    for line in input_data:
        line = line.strip()
        if line.startswith('>'):
            current_label = line[1:]
            sequences[current_label] = ""
        else:
            sequences[current_label] += line

def solution(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

max_gc_label = ""
max_gc_content = 0

for label, sequence in sequences.items():
    gc_content = solution(sequence)
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_label = label

print(max_gc_label)
print(f"{max_gc_content:.6f}")
