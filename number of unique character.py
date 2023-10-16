4.Number of unique character 

def count_unique_characters(input_string):

    unique_characters = set()
    for char in input_string:
        if char.isalpha():
            unique_characters.add(char)
    return len(unique_characters)

input_string = "GUVI GEEK NETWORK PRIVATE LIMITED"
result = count_unique_characters(input_string)
print(result) 