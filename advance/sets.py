"""
intro--> it is a unordered collection of unique items
	--> example: set doesnot support indexing
	--> it is used for remove duplicacy from list
	--> sets are faster than dictionaries
"""


sets_any ={"sunday","monday","tuesday"}
any_list = [1,2,1,5,9,4,6,8,9,4,6,2,3]
set_convert = set(any_list)
print(set_convert)
# again convert to list 
list_convert = list(set_convert)
print(list_convert)
one_line_list_set_list = list(set(any_list))
print(one_line_list_set_list)

"""
2) More about sets:
--> sets also have in keyword for conditional and looping statement
--> It is also used in maths such as --> union and intersection
"""

set1 = {"k","r","i","t","i","k","a"}
print(set1)

if "r" in set1:
	print("Present")
else:
	print("Not present")

for i in set1:
	print(f"{i}-->0")


set2 = {"m","a","h","a","r","s","h","i"}

union_set = set1 | set2
intersection_set = set1 & set2

print(f'The union of two sets are: --> {union_set}')
print(f'The intersection of two sets are: --> {intersection_set}')