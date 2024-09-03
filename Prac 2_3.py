'''
Output the nucleotide bases of DNA sequence
Hiruni Anjana
09/03/2023
'''

#Define the countA, countC, countT and countG variables
countA = 0
countC = 0
countT = 0
countG = 0

#Read the FASTA file and store it in the variable file
with open("sequence.fasta", "r")as file:

    #Read the lines of the file
    for lines in file:

        #Remove the fasta header and escape characters
        if '>' not in lines and lines != '/n':

            for base in lines:
            #Check whether the A,T,C,G bases are there in the lines separately
            #Increment the countA, countC, countT and countG variables separately
                if base == "A":
                    countA += 1
                elif base == "C":
                    countC += 1
                elif base == "T":
                    countT += 1
                elif base == "G":
                    countG += 1

print("Adenine count: ", countA)
print("Cytosine count: ", countC)
print("Thymine count: ", countT)
print("Guanine count: ", countG)

