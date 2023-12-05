#input the users name and age
name_age = input().split()
name = name_age[0]
# if the name equals to -1, it stops the input
while name != '−1':
    try:
        age = int(name_age[1]) + 1
    except ValueError:
        age = 0
    # prints the answer
    print(f'{name} {age}')

# Get next line
    name_age = input().split()
    name = name_age[0]