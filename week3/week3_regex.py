import re

# meta characters
# [] . ^ $ * + ? {} () \ |

#special sequences
#https://pynative.com/python-regex-special-sequences-and-character-classes/

# regex tool
# https://regex101.com/


# findall
string = 'hello 12 hi 8987. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string) 
print(result)

# findall
re.findall('[D-F]', "life is Cool")

# search
string = "My iPython is fun aPython"
match = re.search('Python', string)
match.group()

# match
string = '39801 356, 2102 1111'
# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'
# match variable contains a Match object. 
match = re.search(pattern, string) 

match.group(1)
match.group(2)
match.group(1, 2)
match.groups()

result = re.match("[1-9]{1,3}", "hi 12345 bhey 135456")
result = re.match("[0-9]{1,3}", "12345 dfdf 456")

# split
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string) 
print(result)

result = re.split("\s+", "  Baldan   Gombo") 
print(result)


# sub
string = 'abc 12\
de 23 \n f45 6'
pattern = '\s+'
replace = ''
new_string = re.sub(pattern, replace, string) 
print(new_string)

import re

text = "Dorj Bat. He was born on 17th of February, 1995\
Has got bachelor degree. Phone: 99779977, uses Mobicom. \
Graduated 3rd secondary school of Khovd aimag. \
Citizen ID KhO95021701. PIN code of Khan bank card is 0011\
Lives with his wife and two children."


citizenId = re.findall("\w{2,3}(?=\d{8})\d{8}",text)
region    = re.findall(r"(Khovd|Uvs|Zavkhan)",text)
mobileOperator = re.findall(r"(Mobicom|Unitel|Skytel|G-mobile)",text)
mobile_number  = re.findall("(?<=\s)\d{8}",text)
bank           = re.findall("\s(\w*)\sbank",text)
nChild         = re.findall("\s(\w*)\schildren",text)

