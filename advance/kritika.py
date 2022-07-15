num=int(input("enter a number: "))
generated_list=list(range(0,num+1))

def filter_odd_even(given_list):
    odd_list=[]
    even_list=[]
    for items in given_list:
        if items%2==0:
            even_list.append(items)
        else:
            odd_list.append(items)
    return [odd_list,even_list]

returned_values=filter_odd_even(generated_list)
print(returned_values)

def count_sublists(mixed_list):
    count=0
    for items in mixed_list:
        type_of_element=type(items)
        if type_of_element==list:
            count+=1
    return count

abc=count_sublists(returned_values)
print(abc)
