"""
Mock Exam
Hiruni Anjana
28/02/2023
Output the AC content of the DNA sequence
"""

#Define the sequence variable
sequence = ""

#Read the DNA sequence
with open("seq_q1.fasta", "r")as file:
    #Read the lines of the sequence
    for line in file:
        #Remove the fasta headers
        if line != "\n" and ">" not in line:
            line = line.strip()
            #Add the lines to sequence variable
            sequence = sequence + line

#Total length of the sequence
length = len(sequence)

#A and C counts of the sequence
A_count = sequence.count("A")
C_count = sequence.count("C")

#AC content of the sequnce
AC_content = (A_count + C_count)/length
print("AC content of the sequence: ", AC_content)





