# Detect_plagiarism
# Returns the common subsequence of the two texts
# Vineet Nair
# 01-30-2012
def printLCS(tokenx , i ,  tokeny , j , cc):
    if i == -1 or j == -1 :
        return None
    else:
        if tokenx[i] == tokeny[j]:
            printLCS(tokenx , i-1 , tokeny , j-1 , cc)
            print tokenx[i] ,
            
        elif cc[i][j] == cc[i-1][j]:
            printLCS(tokenx , i-1 , tokeny , j , cc)

        else:
            printLCS(tokenx , i , tokeny , j-1 , cc)

