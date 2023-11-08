# asking for the input from the user
user_input = input()
# splitting the input 
lst = user_input.split()
new_lst = []
for i in lst:
# if the input is more than 0 then add the input to the new list
    if int(i) >= 0:
        new_lst.append(int(i))
# sort the new list to smallest to largest
new_lst.sort()
for j in new_lst:
    print(j, end=" ")