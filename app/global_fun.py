dict = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def maxDate(year,month):
    year=int(year)
    month=int(month)
    if (year%100==0 and year%4==0) or (year%4!=0):
        dict[2]=28
    else:
        dict[2]=29
    return dict[month]

def allDay(year):
    all_day_list = []
    year = int(year)
    for i in range(12):
        max_date=maxDate(year,i+1)
        for j in range(max_date):
            year_month_day = '{0}-{1}-{2}'.format(year,str(i+1).zfill(2),str(j+1).zfill(2))
            all_day_list.append(year_month_day)
    return all_day_list

print(allDay(2020))


