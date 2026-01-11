# Vowel Counter Program

# ask the user for input
text = input("Enter text: ")

# store all vowels
vowels = "aeiouAEIOU"

# start vowel counter
count = 0

# check each character
for ch in text:
    if ch in vowels:  # if character is a vowel
        count += 1

# display result
print("Vowel count:", count)
