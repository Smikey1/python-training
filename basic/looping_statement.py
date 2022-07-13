# i = 0
# while i<10:
#     print(f"Hello Word {i}")
#     i += 1

# for i in range(0,10,2):
#     print(f"for loop {i}")
# user_provied_num = int(input("Please enter any 4 digit num:-->"))
# sum=0
# for i in range(user_provied_num+1):
#     sum += i
# print(f"The final sum is: --> {sum}")

from socket import gaierror


user_provied_num = input("Please enter any 4/5 digit num:-->")
sum=0
# for i in range(len(user_provied_num)):
#     sum += int(user_provied_num[i])
# print(f"The final sum is: --> {sum}")

for i in user_provied_num:
    sum += int(i)
print(f"The final sum is: --> {sum}")


name = input("Please enter your full name:-->")
store = ""
i = 0
while i < len(name):
	if name[i] not in store:
		store += name[i]
		print(f"{name[i]}:{name.lower().count(name[i])}")
	i += 1


# break and continue keyword
for i in range(1,10):
    if i ==5:
        break
    print(f"The new number is: {i}")


guess = 1
win = 10
game_over = False
num= int(input("Please enter any number:-->"))

while not game_over:
    if num == win:
        print(f"you win and u guess in {guess} time.")
        game_over=True
    else:
        if num <win:
            print("Too low") 
        else:
            print("Too high")  
    guess +=1
    num= int(input("guess again")) 