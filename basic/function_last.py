def give_me(last_name,age,first_name="Apple"):
    return f"Your full name is {first_name} {last_name} and your age is {age}"

personal_details = give_me(age=21,last_name="Deo",first_name="Kiran")
print(personal_details)


# global parameter vs local parameter

any_value = 10  # global variable

def any_function(abc,cde):
    any_value=11
    # any_value = 7  # local variable
    print(any_value)

print(any_function(abc="age"))
print(any_value)


