'''
    Algorithms - Practical No.: 1 - Rod Cuttting Problem
    Jaisal Shah - 002 - MSc. C.S.
    Date: 08/09/2021
'''


def rodCutting(rodLength, cutPrices):
    matrix = [[0 for i in range(rodLength + 1)]
              for j in range(rodLength + 1)]
    for i in range(1, rodLength + 1):
        for j in range(1, rodLength + 1):
            if i == j:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j] + cutPrices[i])
            elif i > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i]
                                   [j-i] + cutPrices[i])

    print("Matrix Calculations: ")
    for i in range(1, len(matrix)):
        print(matrix[i][1:])
        print()
    return matrix[rodLength][rodLength]


rodLength = int(input("Size of Rod: "))
cutPrices = {}
for i in range(1, rodLength + 1):
    cutPrices[i] = int(input(f"Price for cut of size {i}: "))

print("The best cost that can be achieved is ",
      rodCutting(rodLength, cutPrices))
