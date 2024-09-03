"""
Mock Exam
Hiruni Anjana
28/02/2023
Output the AC content of the DNA sequence
"""

sequence = ""

with open("seq_q1.fasta", 'r') as file:
    # Declare the variables countA, countT, countC countG and count to 0.
    countA = 0
    countT = 0
    countC = 0
    countG = 0
    count = 0
    # Read each line in the file
    for line in file:
        if ">" not in line and line != "\n":
            line = line.strip()
            sequence = sequence + line

#Read each bases in the file.
for base in sequence:
    # If else statements to check each bases.
    if base == "A":
        countA += 1
    elif base == "T":
        countT += 1
    elif base == "C":
        countC += 1
    elif base == "G":
        countG += 1
    else:
        count += 1

print("Adenine count :" + str(countA))
print("Thymine count :" + str(countT))
print("Cytosine count :" + str(countC))
print("Guanine count :" + str(countG))
print("Non standard count :" + str(count))