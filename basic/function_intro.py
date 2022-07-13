# function define with parameter
def name(yutaValueChaiyo="OK"):
    return f"Kritika Deo {yutaValueChaiyo}"

# function calling with argument
# print(name(", Hello"))

my_value=name("Kritika")
print(my_value)


'''def check_odd_even(anyNum):
    if anyNum %2 == 0:
        return True
    return False'''

'''def check_odd_even(anyNum):
    return anyNum %2 == 0


def check_palindrome(anyNum):
    return anyNum == anyNum[::-1]

userLeDinxa = int(input(" Dear, User yuta value deu -->:"))
function_le_returned_gareko_value= check_odd_even(userLeDinxa)
print(function_le_returned_gareko_value)'''


first,second,third = input("User duita value deu-->:").split(",")
def greater(a,b):
    if a>b:
        return a
    else:
        return b

'''def greatest(a,b,c):
    greater_of_two_num = greater(a,b)
    return greater(greater_of_two_num,c)'''

def greatest(a,b,c):
    return greater(greater(a,b),c)

anything=greatest(int(first),int(second),int(third))
print(anything)