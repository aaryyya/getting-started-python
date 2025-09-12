count=1
while count<=5:
    print(1)
    count+=1
i=5
print("Descending count")
while i>=1:
    print(i)
    i=i-1

print("Traverse in List")
j=0
nums=[1,2,3,45,8,7,9,3,2,7,4,18,7,1,8,4] 
while j<len(nums):
    print(nums[j])
    j+=1

print("elements at a which index")
j=5
i=0
num=(4,6,586,5,2,4,7,12,3,1,24,5)
while i<len(num):
    if(num[i]==j):
        print(j,"element found at index",i)
    i=i+1

print("Values in list")
veggie=["patataaaoooo","brinnjal","ladyskafinger","cucumber"]
for val in veggie:
    print(val)
else:
    print("ENDDDD")

print("Values in tuples")
tup=(1,2,3,5,6,7,8,9,4)
for val in tup:
    print(val)


print("continue word")
k=1
while k<=10:
    if(k%2!=0):
        k+=1
        continue #skips
    print(k)
    k+=1



print("break word")
num=(4,6,586,5,2,4,7,12,3,1,24,5)
i=0
j=12
while i<len(num):
    if(num[i]==j):
        print(j,"element found at index",i)
        break
    else:
        print("finding")
        i=i+1
print("end of loop")


print("for loop")
list=[5,8,5,8,1,6]
for el in list:
    print(el)

print("for loop + else")
for el in list:
    print(el)
else:
    print("END")


str="aryamaheshpatil"
for char in str:
    if(char=='m'):
        print("m found")
        break
    print(char)
else: 
    print("end")

print("Range Syntax in for loops")
seq=range(5)
for i in seq:
    print(i)
print("range")
for j in range(10):
    print(j)
print("range with everything defined")
for k in range(3,12,3):
    print(k)

for i in range(5):
    pass
print("some work")


n=7
sum=0
for i in range(1,n+1):
    sum+=i
print("Total Sum",sum)

n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("Factorial",fact)