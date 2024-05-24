print("{:>75}".format("*********FORMATTED EMAIL ADDRESSES*********"))
# Task 1: Code Correction

# You are given a piece of code that is intended to extract 
# email addresses from a given text. However, the code contains
# errors and does not function as expected. Your task is to
# identify and correct these errors.

# Correct the regex pattern to capture email addresses effectively.
# Modify the code to handle different cases in email addresses.

import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print()
print(f"EMAILS WITH MATCHED FORMAT: {emails}")
print()

# Task 1: Email Extraction Enhancement

# You have a script that extracts email addresses from a 
# text but needs to be refined to exclude certain domains 
# (e.g., 'exclude.com'). Modify the script to extract all 
# email addresses except those from the specified domain.

# Adapt the regex pattern to exclude email addresses from 'exclude.com'.
# Ensure the script still extracts all other valid email addresses.

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

replaceEmail = re.sub(r'\b[A-Za-z0-9._%+-]+@exclude\.com\b', '', text)

emailsWithoutExclude = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', replaceEmail)
print()
print(f"EMAILS WITHOUT 'EXCLUDE.COM' IN EMAIL ADDRESS: {emailsWithoutExclude}")
print()

# Task 1: Advanced Data Extraction

# Problem Statement:
# Develop a script to extract specific information from a 
# formatted text. The text contains data entries delimited by 
# semicolons and formatted as 'Key: Value'. Extract the value 
# corresponding to a specific key.

# Correctly identify and categorize valid and invalid URLs from the list.
# Use regex to validate the format of each URL.

print("{:>75}".format("*********DATA EXTRACTION*********\n"))

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

extractKey = "Occupation"

occupation = re.search(fr"\b{extractKey}:\s*([^;]+)", text)

if occupation:
    print(f"{extractKey.upper()} : {occupation.group(1).strip()}\n")
else:
    print(f"VALUE FOR '{extractKey}' DOES NOT EXIST!\n")

# Task 1: Product Description Keyword Tagging

# Problem Statement:
# You have a list of product descriptions. Your task is to tag 
# each product based on keywords in the description. For instance, 
# tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' 
# based on relevant keywords found in their descriptions.

# Convert all price formats in the string to a standardized 'USD XX.XX' format.
# Use re.sub() to perform the necessary replacements and format transformations.

print("{:>77}".format("*********PRODUCT DESCRIPTION*********\n"))

import re

descriptions = [
    "Smartphone with 6-inch screen and $300 memory",
    "Cotton t-shirt in medium size for $20.99",
    "Stainless steel kitchen knife set priced at $49"
]

def tagProduct(description):
   
    priceFormat = r'\$[\d,]+(?:\.\d{1,2})?' 
    adjustedDescription = re.sub(priceFormat, 'USD \\g<0>', description)
    return adjustedDescription

adjustedDescription = [tagProduct(descript) for descript in descriptions]

for i, descript in enumerate(adjustedDescription, 1):
    print(f"\nProduct {i}: {descript}\n")
