from platform import freedesktop_os_release


age = int(input("Please provide your age:-->"))
if age > 18:
    print(f"As your age is {age} and you can watch Thor Love & Thunder")
else:
    print(f"As your age is {age} and you can't watch Thor Love & Thunder")

# and ////  or


# age --> 0-5 ==> free
# age -->5 - 60 ==> 200
# age --> 60+  ==> 100

# in and check for empty string

fname = input("please enter your first ")

if fname:
    if "a" in fname:
        print("'a' is present in your name")
    else:
        print("Not present")
else:
    print("please input your name")