#Name: Abdur Raafee Mohammad


import numpy as np

def main():

    text=input("input:")            #takes input as a text

    dict={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,
    'G':6,'H':7,'I':8,'J':9,'I':10,'J':11,'K':12,
    'L':13,'M':14,'N':15,'O':16,'P':17,'Q':18,
    'R':19,'S':20,'T':21,'U':22,'V':23,'W':24,
    'X':25,'Y':26,'Z':27
    }                                           #the dictionary for mapping char to int

    keyMatrix=[[2,0,1],[1,0,1],[1,1,0]]         #the 3*3 matrix used as a key


    inputMatrix=convert_text_to_matrix(text,dict)   #converting the text to matrix
    #matrix_print(inputMatrix,3,3)
    encodedMatrix=matrix_encode(keyMatrix,inputMatrix)      #encoding the input matrix with the key
    #matrix_print(encodedMatrix,3,3)
    decodedMatrix=matrix_decode(keyMatrix,encodedMatrix)    #decoding the encoded matrix with the key
    #matrix_print(decodedMatrix,3,3)

    print(test(inputMatrix,decodedMatrix,3,3))          #testing if the cipher successfully worked

def convert_text_to_matrix(text,dict):          #function for converting text to matrix
    inputMatrix=[[0,0,0],[0,0,0],[0,0,0]]       #input matix intialized elements as zero
    counter=-1
    row=3                                       #row is 3 for our matrices
    column=3                                    #column is 3 for out matrices
    for i in range(row):
        for j in range(column):
            counter=counter+1
            if(counter<len(text)):              # checking boundary of the text
                inputMatrix[i][j]=dict.get(text[counter],0)     # using the dictionary
    return inputMatrix


def matrix_encode(keyMatrix,inputMatrix):       #function for encoding a matrix
    encodedMatrix=[]
    mx=np.matrix(keyMatrix)
    my=np.matrix(inputMatrix)
    result=mx*my                                #using numpy for matrix multiplication
    encodedMatrix=result.tolist()
    return encodedMatrix


def matrix_decode(keyMatrix,encodedMatrix):     #function for decoding matrix
    decodedMatrix=[]
    mx=np.matrix(keyMatrix)
    mx=np.linalg.inv(mx)                        #using numpy linalg library for matrix inversion
    my=np.matrix(encodedMatrix)
    result=mx*my                                #using numpy for matrix multiplication
    decodedMatrix=result.tolist()
    decodedMatrix=convert_float_to_int(decodedMatrix,3,3)       #just beautifying the matrix output
    return decodedMatrix


def matrix_print(matrix,row,column):            #function for printing any matrix
    for i in range(row):                     #this function can be used for testing purpose
        for j in range(column):
            print(matrix[i][j],end=' ')
        print('')


def convert_float_to_int(matrix,row,column):     #function for converting float to int of a matix
    for i in range(row):                      #example: 3.0 turns to 3
        for j in range(column):                     #the encoded matrix always contains integers
            matrix[i][j]=(int)(matrix[i][j])     #the decoded matrix always contains integers
    return matrix

def test(matrix1,matrix2,row,column):           #function for testing
    result= True
    for i in range(row):
        for j in range(column):
            if(matrix1[i][j]!=matrix2[i][j]):   #if any element mismatches it is flagged
                result= False
    return result
main()      # the program starts from here
