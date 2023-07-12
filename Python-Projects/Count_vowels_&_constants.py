# Define  a function which counts vowels and consonants in a word python code

def count_vowels_and_consonants(word) :
    vowels = 0
    consonants = 0

    for char in word :

        if char in 'euioaEUIOA' :
           vowels += 1

        elif char.isalpha() :
            consonants += 1

    return (vowels, consonants)

string = input("Word : ")
print(count_vowels_and_consonants(string))
