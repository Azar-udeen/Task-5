6.Longest common substring


def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a table to store the length of the common substring
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_len = 0  # Length of the longest common substring
    end_index = 0  # Ending index of the longest common substring
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i - 1
    
    # Extract the longest common substring
    longest_substring = str1[end_index - max_len + 1:end_index + 1]
    
    return longest_substring

#Strings
str1 = "abcdef"
str2 = "abef"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)