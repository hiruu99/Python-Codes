'''
Hiruni Anjana
Protein sequene analysis
05/03/2023
'''

from Bio.SeqUtils import ProtParam

with open("aa_seq.fasta") as file1:
    # Read each line in the file
    for line in file1:
    #Remove the escape characters
        if line != "\n":
            line = line.strip()
            #Check the fasta head and assign to header variable
            if ' translated' not in line:

                seq1 = line.replace('*', '')
                #seq1 = line

print(seq1)
# Read in the fasta file
#seq_record = SeqIO.read("aa_seq.fasta", "fasta")

# Calculate the length of the sequence
seq_len = len(seq1)

# Calculate the molecular weight of the sequence
mw = ProtParam.ProteinAnalysis(str(seq1)).molecular_weight()

# Calculate the percentage of alanine and glycine in the sequence
aa_counts = ProtParam.ProteinAnalysis(str(seq1)).get_amino_acids_percent()
ala_percent = aa_counts['A']
gly_percent = aa_counts['G']

# Write the results to a new file
with open("aa_stats.txt", "w") as out_file:
    out_file.write("Length: {}\n".format(seq_len))
    out_file.write("Molecular weight: {:.2f}\n".format(mw))
    out_file.write("Alanine percentage: {:.2f}%\n".format(ala_percent))
    out_file.write("Glycine percentage: {:.2f}%\n".format(gly_percent))




