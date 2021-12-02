with open('day1-1-data.txt', 'r') as f:
	lines = f.readlines()
	f.close()

#print(len(lines))
count = 0
countOpp = 0
lines = list(map(lambda n: int(n), lines))
#print(lines)
for i in range(len(lines)-3):

	if lines[i+3] > lines[i]: count = count + 1
	else: 
		countOpp = countOpp + 1

print(count, countOpp)
