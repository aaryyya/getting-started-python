# marks=[15,13,11,12,16,17]
# print(marks)
# print(marks[0])
# print(len(marks))
# print(marks[1:3])
# print(marks[-3:-1])

# list=["ary","ahda","jhfviua",1,2,3]
# print(type(list))
# list.append("meow")
# print(list)
# list.sort
# print(list)
# list.sort(reverse=True)
# print(list)
# list.insert(6,5)
# list.insert(6,"cowwww")
# list.insert(7,"baywatch")
# list.insert(8,"kittens")
# list.insert(9,"cats")
# print(list)
# list.reverse
# print(list)
# list.pop(1)
# print(list)
# list.remove("cowwww")
# print(list)

movies=[]
name1=input("Enter Name of movie 1:")
name2=input("Enter Name of movie 2:")
name3=input("Enter Name of movie 3:")
movies.append(input("Enter movie 4: "))

movies.append(name1)
movies.append(name2)
movies.append(name3)

print(movies)

list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("Palindrome") 
else:
    print("not palindrome")
