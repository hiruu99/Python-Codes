"""
Mock Exam
Hiruni Anjana
28/02/2023

"""
class Sequence:

    #Constructor method with input parameters
    def __init__(self, gene_name, gene_ID, sequence):
        self.gene_ID = gene_ID
        self.gene_name = gene_name
        self.sequence = sequence
        self.sequence_length = len(sequence)

#A sub class for DNA sequeneces
class DNAseq(Sequence):
    def __init__(self, Gene_name, Gene_ID,sequence):
        #Using the super method to pass the object variables to the parent class
        super().__init__(Gene_name, Gene_ID,sequence)
        self.Acount = self.Adenine_count()

    #Method to get A content of a sequence
    def Adenine_count(self):
        A_count = self.sequence.count("A")
        return A_count

#A sub class for amino acid sequences
class AAseq(Sequence):
    def __init__(self, Gene_name, Gene_ID, sequence, Uniprot_ID):
        super().__init__(Gene_name, Gene_ID, sequence)
        self.Uniprot_ID = Uniprot_ID

    #Method to get Glycine amino acids of a sequence
    def get_Glycine_content(self):
        G_count = self.sequence.count("G")
        return G_count

if __name__ == "__main__":

    sequence1 = ""
    with open("seq_q31.fasta")as file1:
        for line in file1:
            #Remove escape characters and FASTA header
            if line != "\n" and ">" not in line:
                # Remove the spaces and split the words with tabs
                line = line.strip()
                sequence1 += line

    obj1 = DNAseq("DREB1A", "4347620", sequence1)

    sequence2 = ""
    with open("seq_q32.fasta") as file2:
        for line in file2:
            #Remove escape characters and FASTA header
            if line != "\n" and ">" not in line:
                # Remove the spaces and split the words with tabs
                line = line.strip()
                sequence2 += line


    obj2 = AAseq("DREB1B", "4347623", sequence2, "Q3T5N4")

    print("Adenine count: ", obj1.Acount)
    print("Glycine count: ", obj2.get_Glycine_content())












