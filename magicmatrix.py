row=int(input("ENter row here:"))
col=int(input("ENter col here:"))

magicmatrix=[]
for i in range (row):
    temp=[]
    for j in range (col):
        temp.append(int(input()))
    magicmatrix.append(temp)
print(magicmatrix)


rowsum=0
maxi=0
for i in range (len(magicmatrix)):
    rowsum=0
    for j in range (len(magicmatrix[i])):
        rowsum+=magicmatrix[i][j]
    maxi=max(maxi,rowsum)

colsum=0
maxic=0
for i in range(len(magicmatrix[0])):
    colsum=0
    for j in range (len(magicmatrix)):
        colsum+=magicmatrix[j][i]
    maxic=max(maxic,colsum)



print(maxi)
print(maxic)


# print(magicmatrix[0][0])
def()