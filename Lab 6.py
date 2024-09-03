'''
Answers for Lab 6
Hiruni Anjana
4/1/2023
'''

from Bio import SeqIO
import re

#Assign the count variable to 0
count = 0

#Load the details of the sequence
for sequence in SeqIO.parse("ATdreb2a.fasta", "fasta"):
    print("Sequence ID: ", sequence.id)
    print("Description: ", sequence.description)
    print("Sequence: ", sequence.seq)
    print("Sequence length: ", len(sequence))

#Run the web-based nucleotide blast program on the ATDREB2A sequence
from Bio.Blast import NCBIWWW
from Bio import SeqIO

#Read the fasta file and store it in the file1 variable
file1 = SeqIO.read("ATdreb2a.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", file1.format("fasta"))

#Save the blast output
with open("dreb2a_blast.xml","w") as file:
    file.write(result_handle.read())

#Open the xml file
output = open("dreb2a_blast.xml")

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(output)

#Define an E-value threshold
E_VALUE_THRESH = 0.05

#Print the attributes of each blast hit
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            print("Blast hit title: ", alignment.title)
            print("Alignment length: ", alignment.length)
            print("E-value:", hsp.expect)
            print("Score:", hsp.score)
            print("Hit/subject sequence: ", hsp.sbjct[0:75] + "...")
            print("Hit sequence length: ", len(hsp.sbjct))

            #pattern = re.compile ("[CT]ACGT[GT]C")
            #Identify the blast hits
            mo = re.finditer("[CT]ACGT[GT]C", hsp.sbjct)

            for item in mo:
                #Print the detected sequence fragment and location
                print("Sequence fragment: ", item.group())
                print("Sequence location: ", item.span())
                count += 1

print("No. of blast hits with ABRE element present in the sequence: ", count)

