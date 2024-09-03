'''
Hiruni Anjana
Answers fror lab 13
05/03/2023
'''

from Bio import Entrez, SeqIO

#Define email for Entrez
Entrez.email = "hiruanjana.99@gmail.com"

#Define the list of accessions
accessions = ["AAK43967.1", "AED90870.1", "NP_567720.1", "AAK59861.1"]

#Loop over each accession, retrieve the sequence and save it to a FASTA file
for acc in accessions:
    handle = Entrez.efetch(db="protein", id=acc, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    SeqIO.write(record, f"{acc}.fasta", "fasta")
    handle.close()

