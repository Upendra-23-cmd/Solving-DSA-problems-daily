# Given a string S, count the number of vowels and consonants in the string.
# Only lowercase English letters are present.

# Input Format
# A single string S.

# Output Format
# Print two integers: the number of vowels followed by the number of consonants.

# Constraints
# 1 ≤ len(S) ≤ 10^5
# S contains only lowercase English letters.

# Example Input
# education

# Example Output
# 5 4

def count_vowels_consonants(s):
    vowels = set('aeiou')
    vowel_count = 0
    consonant_count = 0

    for ch in s:
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count

s = "education"
vowel_count, consonant_count = count_vowels_consonants(s)
print(vowel_count, consonant_count)  # Output: 5 4