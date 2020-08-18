def main():

    matrizB = [[39, 14, 27], [21, 83, 92], [31, 12, 43]]


    for i in range(len(matrizB)):
       for j in range(len(matrizB[i])):
           matrizB[i][j] = matrizB[i][j]*7
    print(matrizB)

main()

