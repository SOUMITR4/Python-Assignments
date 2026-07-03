char = input("Enter a single character: ")

if len(char) != 1 or not char.isalpha():
    print("Please enter a valid single alphabetical character.")
else:
    char_lower = char.toLowerCase() if hasattr(char, 'toLowerCase') else char.lower()
    
    vowels = "aeiou"
    
    if char_lower in vowels:
        print(char,"is a vowel")
    else:
        print(char,"is a consonant.")