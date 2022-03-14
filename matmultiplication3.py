import random as rn
import time

def main():
    row=1000
    column=1000
    matrixA=generateMatrix(row,column)
    #matrix_print(matrixA)
    matrixB=generateMatrix(row,column)
    #matrix_print(matrixB)
    start_time=time.time()
    matrixC=matrix_multiplicate(matrixA,matrixB)
    stop_time=time.time()
    print(stop_time-start_time)
    #matrix_print(matrixC)
    start_time=time.time()
    matrixC=matrix_multiplicate_withT(matrixA,matrixB)
    stop_time=time.time()
    print(stop_time-start_time)
    #matrix_print(matrixC)


def generateMatrix(row,column):             #function for generating matix
    result=[]
    for i in range(row):
        temp=[]
        for j in range(column):
            number=rn.randint(0,9)
            temp.append(number)
        result.append(temp)
    return result

def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=' ')
        print('')

def matrix_transpose(matrix):
    row=len(matrix)
    column=len(matrix[0])
    if(row!=column):
        return 0
    else:
        for i in range(0,row-1):
            for j in range(i+1,row):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        return matrix

def matrix_multiplicate(matrixA,matrixB):
    rowA=len(matrixA)
    columnA=len(matrixA[0])
    rowB=len(matrixB)
    columnB=len(matrixB[0])

    matrixC=[]
    for i in range(rowA):
        temp=[]
        for j in range(columnB):
            temp.append(0)
        matrixC.append(temp)

    for i in range(rowA):
        for j in range(columnB):
            for k in range(columnA):
                matrixC[i][j]+= matrixA[i][k]*matrixB[k][j]
    return matrixC

def matrix_multiplicate_withT(matrixA,matrixB):
    rowA=len(matrixA)
    columnA=len(matrixA[0])
    rowB=len(matrixB)
    columnB=len(matrixB[0])

    matrixC=[]
    for i in range(rowA):
        temp=[]
        for j in range(columnB):
            temp.append(0)
        matrixC.append(temp)

    matrixB=matrix_transpose(matrixB)

    for i in range(rowA):
        for j in range(rowB):
            for k in range(columnB):
                matrixC[j][i]+= matrixA[i][k]*matrixB[j][k]

    matrixC=matrix_transpose(matrixC)
    return matrixC

main()
