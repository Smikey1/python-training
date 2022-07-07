'''first_name,second_name = input("Pleae provide your fav fruit (comma seprated):").split(",")
name_type= type(first_name)
print("your full name is-->"+ first_name+" "+second_name)
print(name_type)
# print("type of first name is:-->"+ name_type)
'''
# String Indexing
from dataclasses import replace
from numpy import place


name = "Language"
        # 01234567
        # -7 -6 -5 -4 -3 -2 -1
# print(name[1:7:2])
print(name[::-1])
print(name[-1::-1])
print(len(name))

# String Method
example= "LeArN pYtHon"
print(example.lower())
print(example.upper())
print(example.title())


print(example.count("P"))

'''fullname,char= input("fullname and char:-->").split(",")
char_count = fullname.lower().count(char)
print("Your fullname is: "+fullname+ " 'a' and char count is: "+ str(char_count))   # python 2

print("Your fullname is {} and '{}' character count is {}".format(fullname,char,char_count))  #python 3

print(f"Your fullname is {fullname} and '{char}' character count is {char_count}") #python 3.6
'''

# solved problem with spaces:  lstrip(),rstrip(),strip()
spaces_problem = "      aar     ayama     "
stars = "**********"
print(stars+spaces_problem+stars)
print(stars+spaces_problem.lstrip()+stars)
print(stars+spaces_problem.rstrip()+stars)
print(stars+spaces_problem.strip()+stars)
solved_problem = spaces_problem.replace(" ","")
print(f"The solve of space problem is:{solved_problem}")

replace_example = "Kritita is a beautiful and she is out standing."
print(replace_example.replace("is","was",1))
print(replace_example.find("is",1))


# center() method
example2="python"   #6 char
print(example2.center(4+6+4,"*"))

## String are immutable and assignment operator
example3 = "any"
# example3[1]="N"  # can't do because of immutable
replaced_exampe = example3.replace("n","N")
print(replaced_exampe)

# example3 = example3 + "body"
example3 += "body"
print(example3)
