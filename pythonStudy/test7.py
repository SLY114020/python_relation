from datetime import datetime, timezone, timedelta
import re

now = datetime.now()
print(now)
dt = datetime(2018, 6, 5, 23, 15)
print(dt)
t = dt.timestamp()
print(datetime.fromtimestamp(t))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(type(cday))

def to_timestamp(dt_str, tz_str):
    ret = re.match('UTC([\+\-])(\d){1,2}:00', tz_str)
    zone = 0
    if(ret.group(1) == '+'):
        zone = int(ret.group(2))
    else:
        zone = -int(ret.group(2))
    tz = timezone(timedelta(hours=zone))
    date_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    real_time = datetime(date_time.year, date_time.month, date_time.day,
                        date_time.hour, date_time.minute, date_time.second, tzinfo=tz)
    print(real_time.timestamp())    
    

to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')