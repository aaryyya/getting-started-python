
magicmatrix=[[4,5,6],[8,6,9],[7,1,2]]
rowsum=0
maxi=0
for i in range (len(magicmatrix)):
    rowsum=0
    for j in range (len(magicmatrix[i])):
        rowsum+=magicmatrix[i][j]
    maxi=max(maxi,rowsum)

print(maxi)

print(magicmatrix[0][0])