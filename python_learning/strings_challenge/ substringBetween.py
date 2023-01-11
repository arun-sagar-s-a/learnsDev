# Write your substring_between_letters function here:
def substring_between_letters(word, fp, sp):
    if not fp in word or not sp in word:
        return word
    if word.index(fp) == -1 or word.index(sp) == -1:
        return word
    fi = word.index(fp)
    si = word.index(sp)
    return word[fi+1:si]


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
