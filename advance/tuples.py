'''
------------>  TUPLES  <--------
--------------------------------

0) intro--> it is a ordered collection of items of any data type
	--> most import tuples are immutable. It means once created, cannot be update
	--> no methods like --> append,insert,pop,remove
	--> tuples are faster than list
ex: days=("sunday","monday")

Tuples only allows these things:
--> count() and index() method
--> len function and slicing in tuples
-->days[0]="Friday" --> gives error

'''

days=("sunday","monday","tuesday")
# days1= "sunday","monday" 

print(type(days))
# print(type(days1))
print(len(days))
# days[1]="Tuesday"
print(days[1])

# tuple unpacking (js object de-structing) same value:
day1,day2,day3 = days
print(day2)

# function returning two values

def calculator(num1,num2):
	sum = num1+num2
	multiply = num1*num2
	return sum,multiply


returned_value = calculator(4,5)
print(f"The returned value is: {returned_value }")
print(f"The type of returned value is: {type(returned_value)}")


# List inside tuples:
# tuple_a=(0,1,2,3,4,5,6,7,8,9,10) 

tuple_a=(1,2,3,[4,5,6],7,8,9) 
tuple_b=(1,2,3,4,5,6,7,8,9) 
tuple_a[3][1] = "kritika" 
print(tuple_a)
print(min(tuple_b))
print(max(tuple_b))
print(sum(tuple_b))

# More about tuples:
# creating new tuple from range function as like list
new_tuples= tuple(range(1,11))
print(new_tuples)

create_list_from_tuples= list(new_tuples)
print(f"The list is: {create_list_from_tuples} and its type is: {type(create_list_from_tuples)}")
create_string_from_tuples= str(new_tuples)
# "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"
print(f"The string is: {create_string_from_tuples} and its type is: {type(create_string_from_tuples)}")
