'''
Hiruni Anjana
Translate the sequence
05/03/2023
'''

from Bio.Seq import Seq

#Read the file
with open("mRNA_seq.fasta") as file1:
    # Read each line in the file
    for line in file1:
    #Remove the escape characters
        if line != "\n":
            line = line.strip()
            #Check the fasta head and assign to header variable
            if '>' not in line:
                seq1 = line
                sequence = Seq(seq1)
                sequence = sequence.translate()


#Write the file in a new fasta file
f=open("aa_seq.fasta", "w")
#Add the transcribed word after the fasta header
f.write(" translated\n" +str(sequence))
#Close the file
f.close()
