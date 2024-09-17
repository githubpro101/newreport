from datetime import timedelta,date
ini_time_for_now = date.today()
print ("initial_date", str(ini_time_for_now))
past_date_before_2yrs = ini_time_for_now - timedelta(days = 730)
today=past_date_before_2yrs.strftime("%m/%d/%y").replace("/0","/").lstrip("0")
print('past_date_before_2yrs:', str(today))
