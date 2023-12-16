def add_time(start, duration, day = False):
  
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  
    start_time = start.partition(":")
    start_minutes_time = start_time[2].partition(" ")
    start_hours = int(start_time[0])
    start_minutes = int(start_minutes_time[0])
    am_pm = start_minutes_time[2]
    am_pm_flip = {"AM": "PM", "PM": "AM"}

    duration_time = duration.split(":")
    duration_hours = int(duration_time[0])
    duration_minutes = int(duration_time[1])
  
    amount_of_days = int(duration_hours / 24)

    total_minutes = start_minutes + duration_minutes
    if total_minutes >= 60:
        start_hours += 1
        total_minutes = total_minutes % 60
    if total_minutes <= 9:
      total_minutes = "0" + str(total_minutes)
    else:
      total_minutes = str(total_minutes)

    total_hours = (start_hours + duration_hours) % 12
    if total_hours == 0:
        total_hours = 12
  
    amount_am_pm_flips = int((start_hours + duration_hours) / 12)
  
    if am_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
        amount_of_days += 1

    if amount_am_pm_flips % 2 == 1:
      am_pm = am_pm_flip[am_pm]
  
    new_time = f"{total_hours}:{total_minutes} {am_pm}"
  
    if day:
        day = day.lower()
        index = (day_of_week.index(day.capitalize()) + amount_of_days) % 7
        new_day = day_of_week[index]
        new_time += f", {new_day}"
      
    if(amount_of_days == 1):
        return f"{new_time} (next day)"
      
    elif(amount_of_days > 1):
        return f"{new_time} ({amount_of_days} days later)"
  
    return new_time