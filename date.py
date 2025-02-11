import datetime

def format_date():
    date_str = input("Enter the date (mm/dd/yyyy): ")
    
    if len(date_str) != 10 or date_str[2] != '/' or date_str[5] != '/':
        print("Invalid date format. Please use mm/dd/yyyy")
        return
    
    month, day, year = date_str.split('/')
    
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        print("Invalid date format. Please use mm/dd/yyyy")
        return
    
    month = int(month)
    day = int(day)
    year = int(year)
    
    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Invalid date. Please enter a valid date.")
        return
    
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    print("Date Output:", months[month - 1], day, ",", year)

format_date()
