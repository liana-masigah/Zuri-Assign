# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if sorted(word) != sorted(anagram):
        return False

    else:
        return True

anagram1 = find_anagram("hello", "check")
anagram2 = find_anagram("below", "elbow")

print(anagram1)
print(anagram2)

