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
outgoing_calls = set(call[0] for call in calls)
receiving_calls = set(call[1] for call in calls)
outgoing_messages = set(text[0] for text in texts)
receiving_messages = set(text[1] for text in texts)

telemarketers = []

for call in outgoing_calls:
    if call not in receiving_calls and call not in outgoing_messages and call not in receiving_messages:
        telemarketers.append(call)


print("Thes numbers could be telemarketers: ")
for call in telemarketers:
    print(call)
