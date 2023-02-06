from itertools import groupby

sequence = "1113122113"
steps = 0
while steps < 50:
    new_sequence = ''.join(str(len(list(v))) + k for k, v in groupby(sequence))
    sequence = new_sequence
    if steps == 39:
        length_1 = len(sequence)
    steps += 1

print(f"The length of the sequence in the 40th step is: {length_1}")
print(f"The length of the sequence in the 50th step is: {len(sequence)}")