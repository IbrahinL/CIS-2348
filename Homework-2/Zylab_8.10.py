def sentencePalindrome(word):
    l, h = 0, len(word) - 1

    # Lowercase string
    word = word.lower()

    # Comparing characters until they equal
    while (l <= h):
        # compares the left side the word
        if (not (word[l] >= 'a' and word[l] <= 'z')):
            l += 1

        # compares the right side of the word
        elif (not (word[h] >= 'a' and word[h] <= 'z')):
            h -= 1

        # If characters are equal
        elif (word[l] == word[h]):
            l += 1
            h -= 1

        # If characters do not equal than it's not a palindrome
        else:
            return False
    # Returns true if sentence is palindrome
    return True


# test sentencePalindrome(word)
word = str(input())
if (sentencePalindrome(word)):
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')