"""
Mock Exam
Hiruni Anjana
28/02/2023
Hydrophobicity score
"""

sequence = ""

#Define the dictionary
GES_SCALE = {'F':-3.7,'M':-3.4,'I':-3.1,'L':-2.8,'V':-2.6,'C':-2.0,'W':-1.9,'A':-1.6,'T':-1.2,'G':-.0,
'S':-0.6,'P': 0.2,'Y': 0.7,'H': 3.0,'Q': 4.1,'N': 4.8,'E': 8.2,'K': 8.8,'D': 9.2,'R':12.3}

#Read the amino acid sequence
with open("seq_q2.fasta", "r") as file:
    for line in file:
        # Remove the escape characters and FASTA header
        if line != '\n' and '>' not in line:
            line = line.strip()
            sequence = sequence + line

H_score = 0

for aa in sequence:
    H = GES_SCALE[aa]
    H_score = H_score + H

print("Hydrophobicity score: ", H_score)





