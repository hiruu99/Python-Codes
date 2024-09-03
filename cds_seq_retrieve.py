'''
Hiruni Anjana
Answers fror lab 13
05/03/2023
'''

from Bio import Entrez

#Take the accession number as user input
accession = input("Enter the accession number: ")

Entrez.email = "hiruanjana.99@gmail.com"

handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
#record = SeqIO.read(handle, "genbank")

file = open("cds_seq.fasta", "w")
file.write(handle.read())
file.close()