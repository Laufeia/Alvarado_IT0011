text = input("Enter a sentence: ")

vowels = "aeiouAEIOU" 
vowel_count = 0
consonant_count = 0
space_count = 0
other_count = 0

for char in text:
    if char in vowels: 
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

# Print the counts
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Spaces:", space_count)
print("Other Characters:", other_count)