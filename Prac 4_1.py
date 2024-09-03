'''
Answers for Lab 4
Hiruni Anjana
09/03/2023
'''

#Method to get the AT count
def calculateAT(file):
    count = 0

    #Read each line in the file
    for base in file:

        #Check whether the base is equal to Adenine(A) or Thymine(T)
        if base == "A" or base == "T":
            count += 1

    #Equation for getting the AT content
    count = (count/len(file))*100

    #Return the AT content
    return "AT content of the DNA sequence: " + str(count)

#Method to split the fasta file
def splitSeq(file):

    #Read the fasta file
    with open(file) as file:
        header = ""
        seq = ""
        diction = {}

        #Read each line in the file
        for line in file:

            #Remove escape characters
            if line != "\n":
                line.strip()

                #Check the fasta header and assign to the header variable
                if ">" in line:
                    header += line
                    seq = ""
                #Check the sequence and assign the lines to seq variable
                else:
                    line = line.strip()
                    seq += line

                #Add values to the dictionary
                diction[header] = seq
        return diction

#Method to check whether the given sequence type is DNA, mRNA or amino acid sequence
def checkSeq(seq):

    #Create a list of amino acids
    aa = ["R", "N", "D", "B", "E", "Q", "Z", "H", "I", "L", "K", "M", "F", "P", "S", "W", "Y", "V"]

    #Read each base in the sequence
    for base in seq:

        #Check whether the base is not in the amino acid list and Uracil base is in the sequence
        if base not in aa and "U" in seq:
            return "mRNA"

        #Check whether the base is in the amino acid list
        elif base in aa:
            return "Amino Acid"

        #Check whether the base is not in the amino acid list and Uracil base is not in the sequence
        elif base not in aa and "U" not in seq:
            return "DNA"

file = "OSDREB_sequences.FASTA"

#Assign the splitSeq function to the dict variable
dict = splitSeq(file)
#print(dict)

#Read the values in the dictionary
for values in dict.values():
    print(values)

    #Assign the checkSeq function to the seq_type variable
    seq_type = checkSeq(values)
    print(seq_type)

    #Check whether the seq_type is equal to DNA
    if seq_type == "DNA":

        #Call the calculateAT method and print the AT content
        print(calculateAT(values))
    else:
        print("AT content: 0")




