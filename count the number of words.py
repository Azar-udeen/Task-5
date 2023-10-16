9.Count the number of words


def count_words(input_string):
    # Split the string into words based on spaces
    words = input_string.split()
    # Return the count of words
    return len(words)

# string:
input_string = "This is a sample sentence."
word_count = count_words(input_string)
print("Number of words:", word_count)