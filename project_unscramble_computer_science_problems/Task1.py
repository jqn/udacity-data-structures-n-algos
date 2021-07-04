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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# initilize and empty list to hold unique numbers
unique_list = []

# traverse all texts records
for number in texts:
    # remove whitespaces and punctuation from phone numbers
    sending_number = number[0].replace("(", "").replace(")", "").replace(" ", "")
    receiving_number = number[1].replace("(", "").replace(")", "").replace(" ", "")
    # check if number exists in unique_list or not
    if sending_number not in unique_list:
        unique_list.append(sending_number)

    if receiving_number not in unique_list:
        unique_list.append(receiving_number)

# traverse all calls records
for number in calls:
    # remove whitespaces and punctuation from phone numbers
    sending_number = number[0].replace("(", "").replace(")", "").replace(" ", "")
    receiving_number = number[1].replace("(", "").replace(")", "").replace(" ", "")
    # check if number exists in unique_list or not
    if sending_number not in unique_list:
        unique_list.append(sending_number)
    
    if receiving_number not in unique_list:
        unique_list.append(receiving_number)

print(f"There are {len(unique_list)} different telephone numbers in the records.")