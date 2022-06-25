import datetime
import calendar


def timecalendar():
    # 范围时间
    holiday_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '12:00', '%Y-%m-%d%H:%M')
    holiday_time_end = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '20:55', '%Y-%m-%d%H:%M')
    work_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '13:00', '%Y-%m-%d%H:%M')
    work_time_end = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '19:55', '%Y-%m-%d%H:%M')
    currentdate = datetime.date.today()
    isworktime = lambda x,y: True if (x>=y[0] and x<y[1]) else False
    workrange=[work_time,work_time_end]
    holidayrange=[holiday_time,holiday_time_end]
    now_time = datetime.datetime.now()
    currentday =calendar.weekday(currentdate.year,currentdate.month,currentdate.day)
    if currentday >= 4: #周五周六周日
        return isworktime(now_time,holidayrange)
    else:
        return isworktime(now_time,workrange)
