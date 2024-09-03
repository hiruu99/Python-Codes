'''
Answers for Question number 2
30/11/2022
Hiruni Anjana
'''


class Sequence:
    sequence_count = 0

    #Constructor
    def __init__(self, gene_name, gene_ID, species_name, subspecies_name, sequence):
        self.gene_ID = gene_ID
        self.gene_name = gene_name
        self.sequence = sequence
        self.sequence_type = self.get_Seq_Type()
        self.sequence_length = len(sequence)
        self.species_name = species_name
        self.subspecies_name = subspecies_name

        Sequence.sequence_count += 1

    @staticmethod
    #Method to split the FASTA file
    def fasta_Split(file):

        #Read the FASTA file
        with open(file) as file:

            header = ""
            seq = ""
            diction = {}

            #Read each line in the file
            for line in file:

                #Remove the escape characters
                if line != '\n':
                    line = line.strip()

                #Check the FASTA head and assign the line to header variable
                if '>' in line:

                    #Strip the line at ">" and split the line at "-"
                    line = line.strip(">").split('-')

                    #Assign only the 1st item to the header variable
                    header = line[0]

                    #Assign the 1st item and the rest of the header to the seq variable
                    seq = line[0:]

                    #Define a new list
                    seq1 = ""

                #Check the sequence and assign the lines to seq variable
                else:
                    line = line.strip()

                    #Assign the sequence to the seq1 variable
                    seq1 += line

                    #Add both the header and the sequence together to one list
                    seq_final = seq + [seq1]

                    #Add values to the dictionary
                    diction[header] = seq_final

            return diction

    #Method for getting the sequence type
    def get_Seq_Type(self):

            #List of amino acids
            aa = ["R", "N", "D", "B", "E", "Q", "Z", "H", "I", "L", "K", "M", "F", "P", "S", "W", "Y", "V"]

            #Read the bases in the sequence
            for base in self.sequence:

                #Check whether the base is not in the amino acid list and Uracil base is in the sequence
                if base not in aa and "U" in self.sequence:
                    return 'mRNA'

                #Check whether the base is in the amino acid list
                elif base in aa:
                    return 'Ámino acid'

                #Check whether the base is not in the amino acid list and Uracil base is not in the sequence
                elif base not in aa and "U" not in self.sequence:
                    return 'DNA'


    #Method for getting the character count
    def get_Character_Count(self):
        diction = {}

        #Check whether ">" is in the sequence
        if ">" not in self.sequence:

            #Read each bases in the sequence
            for base in self.sequence:

                #Read each character in the bases
                for character in base:

                    if character in diction:
                        diction[character] += 1
                    else:
                        diction[character] = 1
            return diction


if __name__ == "__main__":
    file = "OSDREB_sequences_CDS.FASTA"

    #Assign the fasta_Split function to the fasta_dict variable
    fasta_dict = Sequence.fasta_Split(file)
    print(fasta_dict)

    #Read items in the fasta dictionary
    for items in fasta_dict:
        seq_final = fasta_dict[items]

        #Create the object
        object1 = Sequence(*seq_final)

        #Check whether the object is equal to "DREB1A_CDS"
        if object1.gene_name == "DREB1A_CDS":

            #Print the gene_ID, sequence_length and sequence_type
            print("Gene ID: ", object1.gene_ID)
            print("Sequence length: ", object1.sequence_length)
            print("Sequence type: ", object1.sequence_type)

            #Print the base count of the four bases of DREB1A_CDS
            print("Character count: ", object1.get_Character_Count())




















