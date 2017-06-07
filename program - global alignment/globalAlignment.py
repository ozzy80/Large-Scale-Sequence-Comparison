def matchSequence(a, b):
    if a == b:
        return True
    else:
        return False

gapPenalty = int(input('Unesite koliko zelite da bodujete prazninu: '))
matchScore = int(input('Unesite koliko zelite da bodujete pogodak: '))
mismatchScore = int(input('Unesite koliko zelite da bodujete promasaj: '))

with open('string11.txt', 'r') as f:
    str1 = f.read()
with open('string22.txt', 'r') as f:
    str2 = f.read()

tmp = str1 if len(str1) > len(str2) else str2
str2 = str1 if len(str1) < len(str2) else str2
str1 = tmp
columns, rows = len(str1) + 2, len(str2) + 2

#Setting a matrix
matrix = [[0 for x in range(columns)] for y in range(rows)]
matrix[0][1] = ' '
matrix[0][2:] = str1[:]
matrix[1][0] = ' '
for x in range(2, rows):
    matrix[x][0] = str2[x-2]

#Scoring the matrix
for x in range(2, rows):
    matrix[x][1] = matrix[x-1][1] + gapPenalty
for x in range(2, columns):
    matrix[1][x] = matrix[1][x-1] + gapPenalty

for x in range(2, rows):
    for y in range(2, columns):
        matrix[x][y] = max(matrix[x-1][y] + gapPenalty, \
                                matrix[x][y-1] + gapPenalty, \
                                matrix[x-1][y-1] + matchScore if matchSequence(matrix[x][0], matrix[0][y]) else matrix[x-1][y-1] + mismatchScore)


#printing the matrix
print('Matrica skora:')
for i in range(0, rows):
    for j in range(0, columns):
        if i == 0 and j == 0:
            print("", end = '\t')
            continue
        print("{0:>5}".format(matrix[i][j]), end = '\t')
    print()
print()

result1 = str1
result2 = ''
i = rows - 1
j = columns - 1

#best global alignment in matrix using back-tracking pointers
while i != 1 and j != 1:
    scoreDiagonal = matrix[i - 1][j - 1] + matchScore if matchSequence(matrix[i][0], matrix[0][j]) else matrix[i-1][j-1] + mismatchScore
    scoreLeft = matrix[i][j - 1] + gapPenalty
    scoreUp = matrix[i - 1][j] + gapPenalty
    if matrix[i][j] == scoreDiagonal:
        result2 = str2[i-2] + result2
        i -= 1
        j -= 1
        continue
    if matrix[i][j] == scoreUp:
        result2 = '-' + result2
        i -= 1
        continue
    if matrix[i][j] == scoreLeft:
        result2 = '-' + result2
        j -= 1
        continue


#filling result if loop not break on (1,1)
result2 = '-'*(j-1) + result2
result2 = '-'*(i-1) + result2

print('Poravnanje sekvenci: ')
print(result1)
print(result2)