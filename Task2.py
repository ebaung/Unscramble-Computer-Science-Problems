"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
max_call_duration = 0
max_call_number = ""

callers = {}
for each_line in calls:
    if each_line[0] not in callers:
        callers[each_line[0]] = int(each_line[3])
    else:
        callers[each_line[0]] += int(each_line[3])
        
    if each_line[1] not in callers:
        callers[each_line[1]] = int(each_line[3])
    else:
        callers[each_line[1]] += int(each_line[3])
        
max_caller = (max(callers.items(),key = lambda i : i[1]))
max_call_number = max_caller[0]
max_call_duration = max_caller[1]

        
        
print("{} <telephone number> spent the longest time, {} <total time> seconds, on the phone during September 2016.".format(max_call_number,max_call_duration))
