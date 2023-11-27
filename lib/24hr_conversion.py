def convert_time (hour, minute, period):
    if period == "am" and hour == 12:
        hour = 0

    elif period == "pm" and hour != 12:
        hour += 12

    format_time = f"{hour:02d}{minute:02d}"

    return f"The time in 24-hr format is {format_time} hrs"

print(convert_time(8,40,"am"))
print(convert_time(8,40,"pm"))
print(convert_time(12,00,"am"))
print(convert_time(12,15,"am"))
print(convert_time(12,15,"pm"))
