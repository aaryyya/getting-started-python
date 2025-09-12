# def sum(a,b):
#     c=a+b
#     return c

# print(sum(1,6))


# def calc_avg(a,b,c):
#     d=(a+b+c)/3
#     return d

# print(calc_avg(4,2,3))

cities=["mumbai","pune","Satara"]
heros=["iron man","cap","witch","blackwidow","panther","wasp","drstrange"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)

def print_list(list):
    for item in list:
        print(item,end=" ")#end with space insetead on new line print

print_list(heros)