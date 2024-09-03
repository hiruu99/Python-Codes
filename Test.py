from Bio import SeqIO
from Bio import Entrez

accession = input("Enter the accession number: ")
Entrez.email = "hiruanjana.99@gmail.com"

handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()
print(record.id)
print(record.name)
print(record.description)
print(record.seq)
seq =""
seq = record.seq

file = open("cds_seq.fasta", "w")
file.write(str(seq))
file.close()