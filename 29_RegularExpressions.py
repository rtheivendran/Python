import re

#Special characters: (+ ? . * ^ $ ( ) [ ] { } | \)

with open("./Data/regex.txt") as f:
    text_to_search = f.read()

#Find abc
print("\nExample 1: Finding all string abc...")
pattern = re.compile(r'abc|ABC')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print("\nExample 2: Finding all string mixed case abc...")
pattern = re.compile(r'(a|A)(b|B)(c|C)')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print("\nExample 3: Finding all string mixed case abc...")
pattern = re.compile(r'[aA][bB][cC]')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


#Find all digits
print("\nExample 4: Finding all digits...")
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


#Find all phone numbers
print("\nExample 5: Finding all phone numbers...")
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all phone numbers
print("\nExample 6: Finding all phone numbers...")
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


#Find all 800, 900 phone numbers
print("\nExample 7: Finding all 800,900 phone numbers...")
pattern = re.compile(r'[89]00[-]\d\d\d[-]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


#Find all a to z
print("\nExample 8: Finding all lower & upper case alphabets...")
pattern = re.compile(r'[a-zA-Z]')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all 3 character strings ending with "at" except "bat"
print("\nExample 9: Finding all 3 character strings ending with at except bat")
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all phone numbers
print("\nExample 10: Finding all phone numbers...")
pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all Mr
print("\nExample 11: Finding all Mr...")
pattern = re.compile(r'Mr\.?\s[A-Z]\.?\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all Mr, Mrs and Ms
print("\nExample 12: Finding all Mr, Mrs and Ms...")
pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\.?\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all email addressess
print("\nExample 13: Finding all email address...")
pattern = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.(com|net|edu)')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all email addressess
print("\nExample 14: Finding all email address...")
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all URL
print("\nExample 15: Finding all URL...")
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#Find all URL using group
print("\nExample 16: Finding all URL...")
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(text_to_search)

for match in matches:
    print("Groups = {}, {}, {}, {}".format(match.group(0), match.group(1), match.group(2), match.group(3)))
