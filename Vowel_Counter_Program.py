# Vowel Counter Program

text = input("enter a word or sentence:").lower() # Ask user for input
count = 0                                         # Start vowel count at 0

for letter in text:                               # Loop through each character
    if letter in "aeiou":                         # Check if it is a vowel
        count += 1                                # Add 1 if vowel is found

print("Number of vowels:", count)                 # Show total number of vowel