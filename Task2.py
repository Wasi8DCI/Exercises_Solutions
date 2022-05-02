from datetime import datetime
#d = datetime(2020, 12, 25);
#if d.weekday() > 4:
    #print 'Given date is weekend.'
#else:
    #print 'Given data is weekday.'
#To understand the concept of weekday in a week and comparing them with weekend.
#Monday -> 0
#Tuesday -> 1
#Wednesday -> 2
#Thursday -> 3
#Friday -> 4
#Saturday -> 5
#Sunday -> 6
import datetime

def isweekend(date=datetime.datetime.now()):
    if date.weekday() > 4: # 5 and 6 > 4
        return True
    return False
print(isweekend(datetime.date(2021, 8, 6)))
print(isweekend(datetime.date(2021, 8, 7)))
print(isweekend(datetime.date(2021, 8, 8)))
print(isweekend(datetime.date(2021, 8, 9)))