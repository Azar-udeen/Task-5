7.Frequent Character

def most_frequent_char(input_string):
    # Create an empty dictionary to store character frequencies
    char_frequency = {}

    # Iterate through the string to count character frequencies
    for char in input_string:
        if char.isalpha():  # Consider only alphabetic characters
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

    # Find the character with the highest frequency
    most_frequent = max(char_frequency, key=char_frequency.get)

    return most_frequent

# Example usage:
input_string = "hello, world"
result = most_frequent_char(input_string)
print("The most frequent character is:", result)