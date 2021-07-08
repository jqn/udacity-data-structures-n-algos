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


# retrive call by month and year
def getMonthDate(timestamp):
    date = timestamp.split("-")
    month = date[1]
    year = date[2].split(" ")[0]
    return f"{month}-{year}"


september_calls = []
for call in calls:
    if getMonthDate(call[2]) == '09-2016':
        september_calls.append(
            {"receiving_number": call[1], "duration": call[3]})

sorted_calls = sorted(september_calls, key=lambda item: int(item["duration"]))

print(f"{sorted_calls[-1]['receiving_number']} spent the longest time, {sorted_calls[-1]['duration']} seconds, on the phone during")
