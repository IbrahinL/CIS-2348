def replace_characters(input_str, replace):
    result = ""
    # the input will be placed inside the loop
    for i in input_str:
        # now the characters of the input are being replaced
        if i in replace:
            result += replace[i]
        else:
            result += i
    return result

input_str = str(input())
# the characters on the left will be replaced by the characters on the right
replace = {
    "i" : "!",
    "m" : "M",
    "a" : "@",
    "B" : "8",
    "o" : ".",
}

output = replace_characters(input_str, replace)
result = output + "q*s"
print(result)