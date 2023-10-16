8.Anagram of each character



def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for accurate comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Test the function
string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(result) 
 # This should print True