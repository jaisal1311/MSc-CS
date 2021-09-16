'''
    Algorithms - Practical No.: 2 - Longest COmmon Subsequence
    Jaisal Shah - 002 - MSc. C.S.
    Date: 16/09/2021
'''

x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']

matrix = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]

for i in range(1, len(matrix)):
    for j in range(1, len(matrix[i])):
        if(x[i - 1] == y[j - 1]):
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i-1]
                               [j-1], matrix[i][j-1])

for i in range(len(matrix)):
    print(matrix[i])

print(f'The longest common subsequence will be of length: {matrix[-1][-1]}')
