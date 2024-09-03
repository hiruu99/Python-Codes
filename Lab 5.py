class Sequence:
    sequence_count = 0

    def __init__(self, gene_name, gene_ID, species_name, subspecies_name, sequence):
        self.sequence = sequence
        self.gene_ID = gene_ID
        self.gene_name = gene_name
        self.sequence_type = self.get_Seq_Type()
        self.sequence_length = len(sequence)
        self.species_name = species_name
        self.subspecies_name = subspecies_name
        Sequence.sequence_count += 1

    @staticmethod
    #Method to split the FASTA file
    def fasta_Split(file):
        with open(file) as file:
            header = ""
            seq = ""
            diction = {}
            for line in file:
                if line != '\n':
                    line = line.strip()
                if '>' in line:
                    line = line.strip(">").split('-')
                    header = line[0]
                    seq = line[0:]
                    seq1 = ""
                else:
                    line = line.strip()
                    seq1 += line
                    seq_final = seq + [seq1]
                    diction[header] = seq_final
            return diction


    #Method for getting the sequence type
    def get_Seq_Type(self):
            aa = ["R", "N", "D", "B", "E", "Q", "Z", "H", "I", "L", "K", "M", "F", "P", "S", "W", "Y", "V"]
            for base in self.sequence:
                if base not in aa and "U" in self.sequence:
                    return 'mRNA'
                elif base in aa:
                    return 'Amino acid'
                elif base not in aa and "U" not in self.sequence:
                    return 'DNA'

    #Method for getting the character count
    def get_Character_Count(self):
        diction = {}
        if ">" not in self.sequence:
           for base in self.sequence:
                for character in base:
                    if character in diction:
                        diction[character] += 1
                    else:
                        diction[character] = 1
        return diction


class DNAseq(Sequence):
    def __init__(self, gene_name, gene_ID, species_name, subspecies_name, sequence):
        super().__init__(gene_name, gene_ID, species_name, subspecies_name, sequence)

        self.AT_content = self.get_ATcontent()
        self.Transcribed_sequence = self.transcribe_Sequence()

    #Method for getting the transcribed sequence
    def transcribe_Sequence(self):
        Transcribed_sequence = self.sequence.replace("T","U")
        return Transcribed_sequence

    #Method for getting the AT content
    def get_ATcontent(self):
        A_count = self.sequence.count('A')
        T_count = self.sequence.count('T')
        baseCountAT = A_count + T_count
        AT_content = (baseCountAT / len(self.sequence)) * 100

        return AT_content


    # def get_ATcontent(self):
    #     count = 0
    #     for base in sequence:
    #         if base == "U":
    #             base = base.replace("U", "T")
    #         if base == "A" or base == "T":
    #             count += 1
    #     AT_content = (count / len(sequence)) * 100
    #     return AT_content

class MRNAseq(Sequence):
    __Amino_acid_codons = {}
    def __init__(self, gene_name, gene_ID, species_name, subspecies_name, sequence):
        super().__init__(gene_name, gene_ID, species_name, subspecies_name, sequence)

        self.AT_content = self.get_ATcontent()
        self.__Amino_acid_codons = self.upload_Codons(file1)
        self.Translated_sequence = self.translate_Sequence()

    # Method for getting the AT content
    def get_ATcontent(self):
        A_count = self.sequence.count('A')
        T_count = self.sequence.count('U')
        baseCountAT = A_count + T_count
        AT_content = (baseCountAT / len(self.sequence)) * 100

        return AT_content
    # #Method for getting the AT content
    # def get_ATcontent(self):
    #     count = 0
    #     for base in sequence:
    #         if base == "U":
    #             base = base.replace("U", "T")
    #         if base == "A" or base == "T":
    #             count += 1
    #     AT_content = (count / len(sequence)) * 100
    #     return AT_content

    @classmethod
    def upload_Codons(cls, file1):
        Key = ""
        AminoAcid = ""
        with open(file1) as file1:
            for line in file1:
                if "#" not in line and line != "\n":
                    line = line.strip().split("\t")
                    Key = (line[0])
                    AminoAcid = (line[2])
                    cls.__Amino_acid_codons[Key] = AminoAcid
        return cls.__Amino_acid_codons

    #Method to translate a given mRNA sequence into its amino acid sequence
    # def translate_Sequence(self):
    #     Amino = ""
    #     for i in range(0, len(sequence), 3):
    #         codon = sequence[i:i + 3]
    #         Amino += Amino_acid_codons[codon]
    #         if codon == 'UAA':
    #             break
    #         if codon == 'UGA':
    #             break
    #         if codon == 'UAG':
    #             break
    #     self.Translated_sequence = Amino
    #     return self.Translated_sequence

    def translate_Sequence(self):
        arr = []
        for i in range(0, len(self.sequence), 3):
            c = (self.sequence[i: i + 3])
            arr.append(c)
        num = 0
        aa = ""
        while num < len(arr):
            c = arr[num]
            aa += str(self.__Amino_acid_codons.get(c))
            self.Translated_sequence = aa
            if c in ["UAA", "UAG", "UGA"]:
                break
            num += 1
        return (self.Translated_sequence)

class Proteinseq(Sequence):
    def __init__(self, gene_name, gene_ID, species_name, subspecies_name, Uniprot_ID, Reviewed_status, sequence):
        super().__init__(gene_name, gene_ID, species_name, subspecies_name, sequence)

        self.Uniprot_ID = Uniprot_ID
        self.Reviewed_status = Reviewed_status
        self.Hydrophobicity = self.get_Hydrophobicity()

    #Method to return the percentage of the total hydrophobic amino acid residues
    def get_Hydrophobicity(self):
        count = 0
        hydro = ["A", "I", "L", "M", "F", "W", "Y", "V"]
        for base in self.sequence:
            if base in hydro:
                count += 1
        self.Hydrophobicity = (count / len(self.sequence)) * 100
        return self.Hydrophobicity

if __name__ == "__main__":

    fasta_dict = Sequence.fasta_Split("OSDREB_sequences.FASTA")

    seqData = []
    # for loop to go through each value of the dictionary
    for seqData in fasta_dict.values():

        # define a set of amino acid letters excluding A, T, G, C amino acids; to improve this better remove 'N'
        listAminoAcids = ['K', 'N', 'R', 'I', 'Q', 'M', 'H', 'P', 'L', 'E', 'D', 'V', 'Y', 'S', 'W', 'F']

        if (1 in [letter in seqData[-1] for letter in listAminoAcids]):
            # Creating objects using 'Proteinseq' subclass
            protein_Object = Proteinseq(*seqData)

            # printing the relevent details of the 'DREB2A_P' protein
            if seqData[0] == "DREB2A_P":
                print("The DREB2A Protein Sequence; ")
                print("\tThe Uniprot ID: ", protein_Object.Uniprot_ID)
                print("\tThe Reviewed Status: ", protein_Object.Reviewed_status)
                print("\tThe Sequence Type: ", protein_Object.sequence_type)
                print("\tThe Amino Acid Composition: ", protein_Object.get_Character_Count())
                print("\tThe Hydrophobicity: ", protein_Object.get_Hydrophobicity(), "%")

        else:
            # Creating objects using 'DNAseq' subclass
            dna_Object = DNAseq(*seqData)
            # Question_02-subquestion_01
            # printing the relevent detailes of the 'OSDREB1A' DNA sequence
            if seqData[0] == "DREB1A_CDS":
                print("The DREB1A DNA sequence; ")
                print("\tGene ID: ", dna_Object.gene_ID)
                print("\tSequence Length: ", dna_Object.sequence_length, "bp")
                print("\tSequence Type: ", dna_Object.sequence_type)
                print("\tAT Content: ", dna_Object.get_ATcontent())

            # Question_02-subquestion_02
            if seqData[0] == "DREB2B_CDS":
                # transcribe the sequence
                transcribed_mRNA = dna_Object.transcribe_Sequence()

                # defined the codon table text file
                file1 = "codon_table.txt"
                # defined the 'aadict' dictionary
                aadict = MRNAseq.upload_Codons(file1)

                # Creating a new object for the resulting transcribed_mRNA sequence
                mRNA_Object = MRNAseq(seqData[0], seqData[1], seqData[2], seqData[3], transcribed_mRNA)

                # printing the relevent detailes of the transcribed_mRNA sequence
                print("The DREB2B mRNA sequence; ")
                print("\tSequence Length: ", mRNA_Object.sequence_length, "bp")
                print("\tSequence Type: ", mRNA_Object.sequence_type)
                print("\tAT Content: ", mRNA_Object.AT_content)
                print("\tTranscribed mRNA Sequence: ", transcribed_mRNA)

                # Question_02-subquestion_03
                print("\tAmino Acid Sequence: ", mRNA_Object.translate_Sequence())
                print("\tLength of the Amino Acid Sequence: ", len(mRNA_Object.translate_Sequence()), "aa")

#Output the number of sequenes
print("Number of sequences: ", Sequence.sequence_count)









































