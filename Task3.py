#!/usr/bin/env python
# coding: utf-8



"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


import re

# PART A
print("PART A")
#find all area codes and mobile prefixes called by people in Bangalore (originating from (080)):
#find all outbound calls made from fixed lines in Bangalore
#b2any = "Bangalore to any number"
b2any_called = []
#collect area codes of all fixed line numbers called
for each_line in calls:
    if each_line[0].startswith("(080)"):
        string_insideParentheses = re.findall(r'\([^()]*\)', each_line[1])
        if string_insideParentheses not in b2any_called:
            b2any_called.append(string_insideParentheses)
        
        #filter out null values from b2any_called list
        b2any_called = list(filter(None, b2any_called))
        #flatten out fixed_lines, from a list of lists into a flat list
        b2any_called_flat = [item for sublist in b2any_called for item in sublist]
 

#collect area codes of all mobile numbers called
for each_line in calls:
    if each_line[0].startswith("(080)"):   
        if ' ' in each_line[1] and len(each_line[1]) <= 11:
            if each_line[1][0:5] not in b2any_called_flat:
                b2any_called_flat.append(each_line[1][0:5])
     

#append known telemarketer prefix 140 to list, if called
for each_line in calls:
    #filter for all numbers starting with 140, numbers must be 10 digits in length
    if each_line[0].startswith("(080)") and each_line[1].startswith("140") and len(each_line[1]) == 10:
        if each_line[1][0:3] not in b2any_called_flat:
            b2any_called_flat.append(each_line[1][0:3])

                
#sort numbers alphanumerically
b2any_called_flat = [str(x) for x in b2any_called_flat]
b2any_called_flat.sort(key=str)

#final printout
print("The numbers called by people in Bangalore have codes:")
for each in b2any_called_flat:
    print(each)             

print(" ")



# Part B: What percentage of calls from fixed lines in Bangalore are made
# to fixed lines also in Bangalore? In other words, of all the calls made
# from a number starting with "(080)", what percentage of these calls
# were made to a number also starting with "(080)"?

# Print the answer as a part of a message::
# "<percentage> percent of calls from fixed lines in Bangalore are calls
# to other fixed lines in Bangalore."
# The percentage should have 2 decimal digits
# """


print("PART B")
#b2b = "Bangalore to Bangalore"
b2b_calls = 0
for each_line in calls:
    if each_line[0].startswith("(080)") and each_line[1].startswith("(080)"):
        b2b_calls += 1
# suppress printout below since it's intermediate output        
# print("There were {} fixed line to fixed line calls in Bangalore.".format(b2b_calls))
# print(" ")


#find all outbound calls made from fixed lines
#b2any = "Bangalore to any number"
b2any = 0
for each_line in calls:
        if each_line[0].startswith("(080)"):
            #optional printout of all outbound calls from landline numbers
            #print(each_line[0], "called", each_line[1])
            b2any += 1
# suppress printout below since it's intermediate output
# print("There were {} outbound calls made from fixed lines.".format(b2any))
# print(" ")

# percentage(%) of landline-to-landline calls made, out of the total number of calls
print("{}/{}, or {} (%) percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(b2b_calls, b2any, round(100*(b2b_calls/b2any),2)))

