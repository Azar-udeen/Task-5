3.Remove vowels

input_string = "GUVI GEEK NETWORK PRIVATE LIMITED"

def remove_vowels(input_string):
    vowels = "AEIOUaeiou"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result



result = remove_vowels(input_string)
print(result)