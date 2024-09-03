'''
Answers for Lab 2
Hiruni Anjana
09/03/2023
'''

#Define the count variable
count = 0

#Read the FASTA file and store it in the variable file
with open("sequence.fasta", "r")as file:

    #Read the lines of the file
    for lines in file:

        #Remove the fasta header and escape characters
        if '>' not in lines and lines != '/n':
            lines = lines.strip()

            #Check whether the A,T,C,G bases are there in the lines
            for bases in lines:

                #Increment the count variable
                count += 1
                    
print("Length of the DNA sequence: ", count)

