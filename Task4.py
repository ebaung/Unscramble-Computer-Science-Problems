#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


# In[2]:


#obj_1 = unique('texts.csv','calls.csv')


# In[3]:


#python Task1.ipynb


# In[4]:


# %run ./Task1.ipynb
# foo()


# In[62]:


def unique_callers(csv_1='texts.csv', csv_2='calls.csv'): 
    
    #import data from csv files
    import csv
    with open(csv_1, 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open(csv_2, 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
  
    # intialize a null list and unique numbers counter
    unique_callers = []
    unique_receivers = []
    unique_callers_count = 0
    unique_receivers_count = 0
    unique_texters = []
    unique_texters_count = 0
    
    # traverse for all elements in calls
                
    # check if callers or receivers exist in unique_list or not    
    for each_line in calls: 
        if each_line[0] not in unique_callers: 
                    unique_callers.append(each_line[0])
                    unique_callers_count += 1
        if each_line[1] not in unique_receivers: 
                    unique_receivers.append(each_line[1])
                    unique_receivers_count += 1           
    
    #scrape all unique texters' numbers (sending and receiving) in texts
    for each_line in texts: 
        if each_line[0] not in unique_texters: 
                    unique_texters.append(each_line[0])
                    unique_texters_count += 1
        if each_line[1] not in unique_texters: 
                    unique_texters.append(each_line[1])
                    unique_texters_count += 1 
    
    #create list of unique callers' tel numbers
    obj_1 = unique_callers
    obj_2 = unique_receivers
    obj_3 = unique_texters
    
    #sort tel numbers alphanumerically
    obj_1 = [str(x) for x in obj_1]
    obj_1.sort(key=str)
    
    obj_2 = [str(x) for x in obj_2]
    obj_2.sort(key=str)
    
    obj_3 = [str(x) for x in obj_3]
    obj_3.sort(key=str)
    
    #enumerate the list of unique telephone numbers
    #obj_1 = list(enumerate(obj_1, 1))
    
    #return obj_1

    print("Altogether, there are {}<count> unique callers' and {} unique receivers' telephone numbers in the records of {}.\n There are {} unique texters' numbers (senders and receivers) in the records of {}.".format(unique_callers_count,unique_receivers_count,csv_2,unique_texters_count,csv_1))

    print("The {} unique callers' telephone numbers are (only first 5 numbers shown for brevity): \n".format(unique_callers_count))
    print(obj_1[0:5])
    print(" ")
    print("The {} unique receivers' telephone numbers are (only first 5 numbers shown for brevity): \n".format(unique_receivers_count))
    print(obj_2[0:5])
    print(" ")
    print("The {} unique texters' telephone numbers are (only first 5 numbers shown for brevity): \n".format(unique_texters_count))
    print(obj_3[0:5])
    
    
    return obj_1, obj_2, obj_3, texts, calls


# In[63]:


obj_1, obj_2, obj_3, texts, calls = unique_callers('texts.csv','calls.csv')


# In[43]:


#these are all the unique callers' numbers in calls
obj_1


# In[44]:


#these are all the unique receiver's numbers in calls
obj_2


# In[64]:


#these are all the unique texters' numbers (both sending and receiving)
obj_3


# In[75]:


texts[0:10]


# In[74]:


texts[-10:-1]


# In[65]:


possible_telemarketers = []
telemarketers = 0
#numbers that make outgoing calls but never send texts
for each_caller in obj_1:
#never send texts or receive texts
    if each_caller not in obj_3:
        if each_caller not in possible_telemarketers:
            possible_telemarketers.append(each_caller)
            telemarketers += 1
#or receive incoming calls
    elif each_caller not in obj_2: #[column 1 = receiving numbers]
        if each_caller not in possible_telemarketers:
            possible_telemarketers.append(each_caller)
            telemarketers += 1


# In[66]:


possible_telemarketers


# In[80]:

print(" ")
print(" ")
print("These {} numbers could be telemarketers: \nCriteria: Numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.".format(telemarketers))
for each in possible_telemarketers:
    print(each)


# In[67]:


telemarketers


# In[56]:


texts[0:3]


# In[77]:


'74064 66270' in obj_3


# In[78]:


'84313 80377' in obj_3

