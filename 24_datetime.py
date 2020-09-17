import datetime

# d = datetime.date(2016, 7, 24)
# d = datetime.date.today()
# print(d, d.day, d.year)

# Monday 0 Sunday 6
# print(d.weekday())
# Monday 1 Sunday 7
# print(d.isoweekday())

# d = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# print(d + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2
# d = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# bday = datetime.date(2021, 3, 5)
# till_bday = bday - d
# print(till_bday, till_bday.days)

# t = datetime.time(9, 30, 25, 100000)
# print(t)

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# print(dt)
# print(dt.time())
# print(dt.date())

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()  # now gives us option for timezone
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

import pytz

# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
# print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)

# to print specific format
dt_mtn = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))
print(dt_mtn.strftime("%B %b, %Y"))

# to convert from date to datetime
dt_str = "July 26 2016"
dt = datetime.datetime.strptime(dt_str, "%B %d %Y")
print(dt)

# strftime - datetime to string
# strptime - string to datetime
