#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
# import csv
# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

# with open('calls.csv', 'r') as f:
#     reader = csv.reader(f)
#     calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def unique(csv_1='texts.csv', csv_2='calls.csv'): 
    
    #import data from csv files
    import csv
    with open(csv_1, 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open(csv_2, 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
  
    # intialize a null list and unique numbers counter
    unique_list = []
    unique_num_count = 0
      
    # traverse for all elements
    imported_files = [texts, calls]
#     for each in imported_files:
#         for each_line in each: 
#             # check if exists in unique_list or not 
#             if each_line[0] not in unique_list: 
#                 unique_list.append(each_line[0])
#                 unique_num_count += 1
#             if each_line[1] not in unique_list: 
#                 unique_list.append(each_line[1])
#                 unique_num_count += 1
                
    for each in imported_files:
        for each_line in each: 
            for i in range(2):
            # check if exists in unique_list or not 
                if each_line[i] not in unique_list: 
                    unique_list.append(each_line[i])
                    unique_num_count += 1
    
    #create list of unique tel numbers
    obj_1 = unique_list
    
    #sort fixed_lines numbers alphanumerically
    obj_1 = [str(x) for x in obj_1]
    obj_1.sort(key=str)
    
    #enumerate the list of unique telephone numbers
    obj_1 = list(enumerate(obj_1, 1))
    
    #return obj_1

    print("Altogether, there are {}<count> different telephone numbers in the records of the 2 csv files {} and {}.\n".format(unique_num_count, csv_1, csv_2))

#     print("The {} unique telephone numbers are: \n".format(unique_num_count))
#     for each in obj_1:
#         print(each)
        


unique('texts.csv','calls.csv')
# print("Altogether, there are {}<count> different telephone numbers in the records of the 2 csv files {} and {}.".format(unique_num_count, csv_1, csv_2))
# print("The {} unique telephone numbers are: {}".format(unique_num_count,unique_list))

