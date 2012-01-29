# Detect_plagiarism
# Vineet Nair
# 01-30-2012

import re
import sys
from PrintLCS import *

# Getting the filenames from the command-line
if (len(sys.argv)) > 2:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
else:
    print " Please give the filenames for comparing after putting it in the local directory .."
    exit()

#Printing the filenames for checking if the correct filename was passed as an argument
print "The first filename is : ", file1
print "The second filename is : " , file2

#linex = open('austen_sample1', 'r').read()
linex = open(file1, 'r').read()

#liney = open('austen_plagiarism1', 'r').read()
liney = open(file2, 'r').read()

# Tokenizing the stringto include only alphanumeric words
tokenizer = re.compile('[a-zA-Z0-9]+', re.IGNORECASE)

#Inserting a null value in the start for including an initial offset element in the algorithm
tokenx= tokenizer.findall(linex)
tokenx.insert(0 , 0)

tokeny = tokenizer.findall(liney)
tokeny.insert(0 , 1)

#Initialising the cost array cc and the length of the common subsequence array ll
cc = [[0 for col in range(len(tokeny)+1)] for row in range(len(tokenx)+1)]
ll = [[0 for col in range(len(tokeny)+1)] for row in range(len(tokenx)+1)]

#The dynamic programming algorithm
for x in range(1 , len(tokenx)):
    for y in range(1 , len(tokeny)):
        if tokenx[x] == tokeny[y]:
            cc[x][y] = cc[x-1][y-1] + len(tokenx[x])**2
            ll[x][y] = ll[x-1][y-1] + 1   
        else:
            if cc[x-1][y] >= cc[x][y-1]:
                ll[x][y] = ll[x-1][y]
                cc[x][y] = cc[x-1][y]
            else:
                ll[x][y] = ll[x][y-1]
                cc[x][y] = cc[x][y-1]

#The recursive algorithm for printing the results
print "The Common subsequence found is , \n <",
printLCS(tokenx , len(tokenx)-1 , tokeny , len(tokeny)-1 , cc )
print ">\n"

p = len(tokenx)-1
q = len(tokeny)-1
print "The total no of words in the original text is " , p , "."
print "The total no of words in the test text is " , q , "."
print "The length of the common subsequence is " , max(max(ll)) , "."
print "The plagiarism value calculated is " , max(max(cc)) , "."