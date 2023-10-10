import re

def is_valid_date(date_str):
    # Check if the date string matches the required format
    pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$"
    return re.match(pattern, date_str) is not None

def parse_date(date_str):
    monthDict = {"January" : 1, "February" : 2, "March" : 3, "April" : 4,
                 "May" : 5, "June" : 6, "July" : 7, "August" : 8, "September" : 9,
                 "October" : 10, "November" : 11, "December" : 12}

    # Extract the month, day, and year from the date string using find()

    year = date_str[date_str.find(',') + 2 : ]

    month, day = date_str[ : date_str.find(',')].split(" ")

    month = monthDict[month.title()]

    return '{}/{}/{}'.format(month, day, year)

#Part A: Read dates from input until -1 is entered
print("Enter dates (format: Month Day, Year):")
dates = []
while True:
    date = input()
    if date == '-1':
        break
    if is_valid_date(date):
         dates.append(parse_date(date))
         print(dates)
# Part B: Read dates from "inputDates.txt" file
with open(r"C:\Users\Ibrahin Leon\Desktop\pycharm\inputDates.txt") as file:
    dates = [parse_date(date) for date in file if is_valid_date(date)]

# Part C: Write correct dates to "parsedDates.txt" file
with open("parsedDates.txt", 'w') as wfile:
    wfile.write(''.join(dates))