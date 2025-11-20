word = "serendipitious"

wovels = ["a","e","i","o","u"]

vowel_count = 0
for char in word:
    if char in wovels:
        vowel_count += 1
print("Number of vowels in the word is:", vowel_count)