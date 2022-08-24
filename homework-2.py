# Use the following list - [1,11,14,5,8,9]
l_1 = [1,11,14,5,8,9]

def list_2(number):
    l_2 = []
    for i in number:
        if i < 10:
            l_2.append(i)
    return l_2

print(list_2(l_1))

#2

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

new_list = l_1 + l_2


new_list= sorted(new_list)
print(new_list)
