def partition(user_ids, i, k):
    low = i - 1
    pivot = user_ids[k]
    for j in range(i, k):
        if pivot >= user_ids[j]:
            low += 1
#comparing the two indexes variable
#determine if the swap is necessary 
            user_ids[low], user_ids[j] = user_ids[j], user_ids[low]
    user_ids[low + 1], user_ids[k] = user_ids[k], user_ids[low + 1]
    return low + 1

# this will determine the number_calls
def quicksort(user_ids, i, k):
    if k > i:
        j = partition(user_ids, i, k)
        quicksort(user_ids, i, j - 1)
        quicksort(user_ids, j + 1, k)

if __name__ == "__main__":
    ID = []
    user_input = input()
# the input ends when the user inputs -1
    while user_input != "-1":
        ID.append(user_input)
        user_input = input()

# organizes list the input, when it begins and ends
    quicksort(ID, 0, len(ID) - 1)

# prints the number of times it went through the quicksort function
    number_calls = int((2 * len(ID)) - 1)
    print(number_calls)
# prints the IDs of the user
    for user_input in ID:
        print(user_input)