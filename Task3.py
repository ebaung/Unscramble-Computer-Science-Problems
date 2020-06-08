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
#find all fixed lines area codes in parentheses (e.g. (080))
fixed_lines = []
for each_line in calls:
    for each in each_line:
        #the following Regex expression finds all string instances within parentheses (including the parentheses)
        string_insideParentheses = re.findall(r'\([^()]*\)', each)
        if string_insideParentheses not in fixed_lines:
            fixed_lines.append(string_insideParentheses)



#find all mobile numbers (e.g. 7890 4928)
mobile_numbers = []
for each_line in calls:
    for each in each_line:
        #filter for all numbers of length 11 that contain a space ' '
        if ' ' in each and len(each) <= 11:
            if each not in mobile_numbers:
                mobile_numbers.append(each)




#find all telemarketers' numbers (e.g. 140xxxxxxxx)
telemkt_numbers = []
for each_line in calls:
    for each in each_line:
        #filter for all numbers starting with 140, numbers must be 10 digits in length
        if each[0:3] == '140' and len(each) == 10:
            if each not in telemkt_numbers:
                telemkt_numbers.append(each)



#filter out null values from fixed_lines list
fixed_lines = list(filter(None, fixed_lines))
fixed_lines



#sort numbers alphanumerically
mobile_numbers = [str(x) for x in mobile_numbers]
mobile_numbers.sort(key=str)



mobile_numbers


#extract only the first 4 digits of each mobile number to get 4-digit the mobile number prefixes
mobile_num_prefixes = []
for each in mobile_numbers:
    if each[0:4] not in mobile_num_prefixes:
        mobile_num_prefixes.append(each[0:4])




mobile_num_prefixes




#flatten out fixed_lines, from a list of lists into a flat list
fixed_lines_flat = [item for sublist in fixed_lines for item in sublist]




fixed_lines_flat




#sort fixed_lines numbers alphanumerically
fixed_lines_flat = [str(x) for x in fixed_lines_flat]
fixed_lines_flat.sort(key=str)




print("The numbers called by people in Bangalore have codes: \n")
print("Fixed lines:")
for each in fixed_lines_flat:
    print(each)
print(" ")


print("Mobile numbers (4 digit prefixes starting with 7, 8, or 9):")
for each in (mobile_num_prefixes):
    print(each)
print(" ")

#sort telemarketers' numbers alphanumerically
telemkt_numbers = [str(x) for x in telemkt_numbers]
telemkt_numbers.sort(key=str)




print("Telemarketers' numbers start with the prefix 140:")
for each in telemkt_numbers:
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

fixed2fixed_calls = 0
for each_line in calls:
    if "(" and ")" in each_line[0] and "(" and ")" in each_line[1]:
        #optional printout of all landline-to-landline calls
        #print(each_line[0], "called", each_line[1])
        fixed2fixed_calls += 1
print("There were {} fixed line to fixed line calls.".format(fixed2fixed_calls))
print(" ")


#find all outbound calls made from fixed lines
fixed_lines_outgoing_calls = 0
for each_line in calls:
        if "(" and ")" in each_line[0]:
            #optional printout of all outbound calls from landline numbers
            #print(each_line[0], "called", each_line[1])
            fixed_lines_outgoing_calls += 1
print("There were {} outbound calls made from fixed lines.".format(fixed_lines_outgoing_calls))
print(" ")

# In[107]:


# percentage(%) of landline-to-landline calls made, out of the total number of calls
print("{}/{}, or {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(fixed2fixed_calls, fixed_lines_outgoing_calls, round(100*(fixed2fixed_calls/fixed_lines_outgoing_calls),2)))

