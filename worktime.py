import datetime
import calendar
def timecalendar():
    currentdate = datetime.date.today()
    #工作日13-20
    #节假日12-21
    workrange=[13,20]
    holidayrange=[12,21]
    isworktime = lambda x,y: True if (x>=y[0] and x<y[1]) else False
    nowhour = datetime.datetime.now().hour
    currentday =calendar.weekday(currentdate.year,currentdate.month,currentdate.day)
    if currentday >= 4:
        return isworktime(nowhour,holidayrange)
    else:
        return isworktime(nowhour,workrange)