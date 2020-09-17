import re

# regular expression is a sequence of characters that
# define a search pattern

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat
pat 
bat
"""

sentence = "Start a sentence and then bring it to an end"

# pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")
# pattern = re.compile(r"[^a-zA-Z]")
# pattern = re.compile(r"[^b]at")
# pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
# pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
pattern = re.compile(r"start", re.IGNORECASE)

# matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search)  # returns a list of strings
matches = pattern.search(sentence)
print(matches)

# for match in matches:
# print(match)

# pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")
# with open("30_data.txt", "r") as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)
