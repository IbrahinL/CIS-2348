def selection_sort_descend_trace(list):
# first for is for the row
    for i in range(len(list) - 1):
        top_num = i
# second for is for the column
        for j in range(i + 1, len(list)):
# the if statement is there to make the highest number goes first
# the rest of the code is making following the pattern of highest to lowest number
            if list[top_num] < list[j]:
                top_num = j
        list[i], list[top_num] = list[top_num], list[i]
        for result in list:
            print(result,end=" ")
        print()
    return list

if __name__ == "__main__":
    list = []

    list = [int(x) for x in input("").split()]
    selection_sort_descend_trace(list)