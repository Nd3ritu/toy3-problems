#the function below converts timf from 12-hr format to 24-hr format 
def convert_time (hour, minute, period): 
    # if statement for defining period "am" and "pm"
    if period == "am" and hour == 12:
        hour = 0

    elif period == "pm" and hour != 12:
        hour += 12
    #adding formatting specification for 2 digits and sets 0 for a single digit
    format_time = f"{hour:02d}{minute:02d}"

    return f"The time in 24-hr format is {format_time} hrs"
#outputs on the terminal
print(convert_time(8,40,"am"))
print(convert_time(8,40,"pm"))
print(convert_time(12,00,"am"))
print(convert_time(12,15,"am"))
print(convert_time(12,15,"pm"))
