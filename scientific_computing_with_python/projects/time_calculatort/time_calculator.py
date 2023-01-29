
def add_time(start, duration, day_of_week=""):
    
    MINS = 60
    HOURS = 24
    DAYS_WEEK = 7
    DAYS_IN_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    HOURS_IN_DAY_KEY = {1:"12 AM", 2:"1 AM", 3:"2 AM", 4:"3 AM", 5:"4 AM", 6:"5 AM", 7:"6 AM", 8:"7 AM", 9:"8 AM", 10:"9 AM", 11:"10 AM", 12:"11 AM", 13:"12 PM", 14:"1 PM", 15:"2 PM", 16:"3 PM", 17:"4 PM", 18:"5 PM", 19:"6 PM", 20:"7 PM", 21:"8 PM", 22:"9 PM", 23:"10 PM", 24:"11 PM"}
    HOURS_IN_DAY_VALUES = {"12 AM":1, "1 AM":2, "2 AM":3, "3 AM":4, "4 AM":5, "5 AM":6, "6 AM":7, "7 AM":8, "8 AM":9, "9 AM":10, "10 AM":11, "11 AM":12, "12 PM":13, "1 PM":14, "2 PM":15, "3 PM":16, "4 PM":17, "5 PM":18, "6 PM":19, "7 PM":20, "8 PM":21, "9 PM":22, "10 PM":23, "11 PM":24}

    days_later = ''
    total_days = 0
    new_day_of_week = ''
    new_hour = ''
    new_min = ''
    new_time = ''
    
    start_hour = int(start.split(":")[0])
    start_min = int((start.split(":")[1]).split(" ")[0])
    start_am_pm = (start.split(":")[1]).split(" ")[1]
    start_time = f"{start_hour} {start_am_pm}"
    start_hour_value = HOURS_IN_DAY_VALUES[start_time]
    duration_hour = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])

    total_min = start_min + duration_min
    if total_min >= MINS:
        new_min = total_min - MINS # this can never be greater than 59
        duration_hour += 1 # this can NEVER be greater than 1
    else:
        new_min = total_min

    total_hour = start_hour_value + duration_hour
    if total_hour > HOURS:
        new_hour_value = (total_hour % HOURS)
        total_days = (total_hour // HOURS)
    else: 
        new_hour_value = total_hour
        
    new_hour = (HOURS_IN_DAY_KEY[new_hour_value]).split(" ")[0]
    new_am_pm = (HOURS_IN_DAY_KEY[new_hour_value]).split(" ")[1]

    new_time = f'{new_hour}:{new_min:02d} {new_am_pm}'

    day_of_week = day_of_week.capitalize()
    if day_of_week in DAYS_IN_WEEK:
        if total_days == 0:
            new_day_of_week = day_of_week
            new_time += f', {new_day_of_week}'
        else:
            day_of_week_index = DAYS_IN_WEEK.index(day_of_week)
            new_day_of_week_index = ((total_days + day_of_week_index) % DAYS_WEEK)
            new_day_of_week = DAYS_IN_WEEK[new_day_of_week_index]
            if total_days == 1:
                new_time += f', {new_day_of_week} (next day)'
            if total_days >= 2:
                new_time += f', {new_day_of_week}'
                new_time += f' ({total_days} days later)'
    else:
        if total_days == 1:
            new_time += f' (next day)'
        if total_days >= 2:
            new_time += f' ({total_days} days later)'

    return new_time
