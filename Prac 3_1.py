'''
Answers for Lab 2
Hiruni Anjana
09/03/2023
'''

#Define the empty dictionary
diction = {}

#Define header and seq variables
header = ""
seq = ""

#Define the amino acid list
aa = ["R", "N", "D", "B", "E", "Q", "Z", "G", "H", "I", "L", "K", "M", "F", "P", "S", "W", "Y", "V"]

#Read the fasta file
with open("OSDREB1A.fasta", "r") as file:

    #Read the lines of the file
    for lines in file:
        if lines != '/n':
            lines = lines.strip()

            #Assign fasta header to header variable and sequence to seq variable
            if '>' in lines:
                header = lines
                seq = ""
            else:
                lines = lines.strip()
                seq += lines

                #Add values to dictionary
                diction[header] = seq

                #Read the each bases in dictionary
                for bases in seq:

                    #Check whether the bases are not in the amino acid list
                    if bases not in aa:

                        #Replace the “T” base with “U” in the sequence
                        sequence = seq.replace("T", "U")

#Open a new fasta file
f = open("OSDREB1A_mRNA.fasta", "w")

#Write the transcribed sequence in the file
f.write(header + " transcribed\n" + sequence)

#Close the file
f.close()

