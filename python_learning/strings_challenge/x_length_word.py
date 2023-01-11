# Write your x_length_words function here:
def x_length_words(word, x):
    count = 0
    for i in word.split(" "):
        if len(i) >= 2:
            count += 1
    if count == len(word.split(" ")):
        return True
    else:
        return False


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
