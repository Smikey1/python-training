'''
intro--> it is a ordered collection of items
ex: number=[1,2,3,4]
words, mixed

'''

# list_of_nepali_names = ["कृतिका, आर्यामा , समय , रुसब , महर्षि"]
import re


list_of_even_numbers=[2,4,6]
list_of_odd_numbers=[1,3,5]

mixed=["one",2,3.0,"Four",False]

for i in mixed:
    print(f"{type(i)}\n")

list_of_odd_numbers[2]=False
print(list_of_odd_numbers[2])

print(type(mixed))

# 2) add data to list --> append() and insert() method
list_of_numbers= [1,2,3,4,5]
list_of_numbers.append(6)
list_of_numbers.insert(2,11)  # position = 2


print(list_of_numbers)

# 3) Remove or delete items from list
fruits1= ["apple","mango","banana"]
fruits2= ["grapes","watermelon","guva","grapes"]
popped_item= fruits1.pop(2)
print(popped_item)
print(fruits1)

# del fruits1[1]
# print(fruits1)

# 4) in keyword in list
if "apple" in fruits1:
    print("present")
else:
    print("not present")

"""
4) More list method
--> count() method
--> sort() method  # it sort in original list
--> sorted() function  
--> clear() and copy() method
--> reverse() method

"""
print(sorted(fruits2))
print(fruits2)
print(fruits2.count("grapes"))
fruits2.sort()
print(fruits2)
list_of_numbers.reverse()
fruits3= fruits2.copy()
print(list_of_numbers)
fruits2.clear()
print(fruits2)
print(fruits3)

# is vs equal   --> comparision
fruits5= ["apple","mango","banana"]
fruits6= ["apple","mango","banana"]

print(fruits5==fruits6)  # check for same value as well as num
print(fruits5 is fruits6)  # check for the location/address of object in 


def give_me_list(num):
    my_list=[]
    for i in range(0,num+1):
        my_list.append(i**2)
    return my_list

mero_list_diyo_hurray= give_me_list(10)
print(mero_list_diyo_hurray)    

given_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def rev_list(any_list):
    any_list.reverse()
    return any_list

ok = rev_list(given_list)
print(ok)

def reverse_a_list(given_lists):
    reversed_list = []
    for item in given_lists:
        popped_item = given_lists.pop()
        reversed_list.append(popped_item)
    return reversed_list



any = ["aryama","kritika","rushav","samaya","maharshi"]
# any = ["amayar","akitira","vahsur","ayamas","ihsraham"]
# reverse this -->
def rev_list(given_list):
    reverse_bhayeko_list=[]
    for items in given_list:
        reverse_bhayeko_list.append(items[::-1])
    return reverse_bhayeko_list

returned_value=rev_list(any)
print(returned_value)


# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# [[1,3,5],[2,4,6]]
