Calculate the Vowels in Guvi Geek Network Private Limited


# Input string
string = "GUVI GEEKS NETWORK PRIVATE LIMITED"

# counts for each vowel
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Convert the input string to uppercase for case-insensitivity
string = string.upper()

# Loop through the characters in the string
for char in input_string:
    if char == 'A':
        count_a += 1
    elif char == 'E':
        count_e += 1
    elif char == 'I':
        count_i += 1
    elif char == 'O':
        count_o += 1
    elif char == 'U':
        count_u += 1

# Calculate the total number of vowels
total_vowels = count_a + count_e + count_i + count_o + count_u

# Print the results
print("Total number of vowels:", total_vowels)
print("Count of 'A':", count_a)
print("Count of 'E':", count_e)
print("Count of 'I':", count_i)
print("Count of 'O':", count_o)
print("Count of 'U':", count_u)
