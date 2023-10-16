5.palindrome

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for a case-insensitive check
    clean_string = ''.join(input_string.split()).lower()
    return clean_string == clean_string[::-1]

 # Output will be True
input_string = "racecar"
result = is_palindrome(input_string)
print(result) 

# Output will be False
input_string = "hello"
result = is_palindrome(input_string)
print(result)  