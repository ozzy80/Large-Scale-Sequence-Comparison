
gepS = -1; #gep score
def matchS(char1, char2): #score if match or mismatch 
	if char1 == char2:
		return 1 
	else: 
		return -1 


with open('string1.txt', 'r') as f:
    str1 = f.read()
with open('string2.txt', 'r') as f:
    str2 = f.read()

first = [' '] + list(str1)
second = [' '] + list(str2)

w, h = len(first), len(second) 								#dimensions of matrix
matrixA = [[0 for x in range(w+1)] for y in range(h+1)] 	#alignment matrix
matrixBTP =[[' ' for x in range(w+1)] for y in range(h+1)]	#back-tracking matrix
fieldMax = 0 												#temporary maximum in the matrix
fieldMaxX, fieldMaxY = 0, 0									#coordinates of the temporary maximum

for x in range(1, w):
	for y in range(1, h):
		#dinamic scoring
		m = matrixA[y][x] = max(0,  \
							matrixA[y-1][x] + gepS,  \
							matrixA[y][x-1] + gepS,  \
							matrixA[y-1][x-1] + matchS(first[x], second[y]) \
							)
		
		#back-track "pointers"
		if m == 0: 							#no pointer
			matrixBTP[y][x] = ' ' 
		elif m == (matrixA[y-1][x] + gepS): #pointer up
			matrixBTP[y][x] = 'U' 
		elif m == (matrixA[y][x-1] + gepS): #pointer left
			matrixBTP[y][x] = 'L'
		else:								#pointer diagonally
			matrixBTP[y][x] = 'D'
			
			
		if fieldMax <= m: 	#temporary maximum in A
			fieldMax = m
			fieldMaxX = x
			fieldMaxY = y

#printing the matrix
print('\nMatrix for scoring: ')
print(' ', end = '\t')
for x in range(0, w):
	print(first[x], end = '\t')
print()
for y in range(0, h):
	print(second[y], end = '\t')
	for x in range(0, w):
		print(matrixA[y][x], end = '\t')
	print()

#direction = 'D' #how I got here
result1 = []
result2 = []
#best local alignment from maximum in matrix with back-tracking pointers
while matrixA[fieldMaxY][fieldMaxX] != 0:

	direction = matrixBTP[fieldMaxY][fieldMaxX] #to next position in matrix	
	if direction == ' ':
		print('error, this shouldn\'t have accured')
		break
	elif direction == 'U':
		result1 = ['-'] + result1
		result2 = [second[fieldMaxY]] + result2
		fieldMaxY -= 1
	elif direction == 'L':
		result1 = [first[fieldMaxX]] + result1
		result2 = ['-'] + result2
		fieldMaxX -= 1
	else:
		result1 = [first[fieldMaxX]] + result1
		result2 = [second[fieldMaxY]] + result2
		fieldMaxX -= 1
		fieldMaxY -= 1
	
	
print('\nBest local alignment from maximum in matrix with back-tracking: ')
print(result1)
print(result2)
						
print('\nEnd of program')