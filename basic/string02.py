'''first_name,second_name = input("Pleae provide your fav fruit (comma seprated):").split(",")
name_type= type(first_name)
print("your full name is-->"+ first_name+" "+second_name)
print(name_type)
# print("type of first name is:-->"+ name_type)
'''
# String Indexing
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
spaces_problem = "      aarayama     "
stars = "**********"
print(stars+spaces_problem+stars)
print(stars+spaces_problem.lstrip()+stars)
print(stars+spaces_problem.rstrip()+stars)
print(stars+spaces_problem.strip()+stars)

