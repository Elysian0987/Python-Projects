# Python program to count the occurrence of each character in a word

def count_characters(word):
    character_counts = {}
    for character in word:
        if character in character_counts:
            character_counts[character] += 1
        else :
            character_counts[character] = 1
    return character_counts

word = input("Enter desired word: ")

character_counts = count_characters(word)

for character, count in character_counts.items():
    print(character,":",count)

# Simplified version 

'''word = input("Enter desired word: ")
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in  char_count.items():
    print(char,count)'''
