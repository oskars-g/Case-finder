import os, datetime


def year_case_finder(year, month, day):
    year = int(year) # python 2.7 nav nepieciešams
    month = int(month)
    day = int(day)
    laiks = datetime.datetime(year, month, day).strftime('%Y%m%d')
    case = []
    for filename in os.listdir('.'):
        if filename.endswith(".sav"):
            db = []
            db.append(filename)
            for i in db:
                if laiks == db[0][:8]:
                    case.append(filename)
                else:
                    continue
    if not case:
        return False
    else:
        return case


def closest_case_finder(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    laiks = datetime.datetime(year, month, day).strftime('%Y%m')
    case = []
    for filename in os.listdir('.'):
        if filename.endswith(".sav"):
            db = []
            db.append(filename)
            for i in db:
                if laiks == db[0][:6]:
                    case.append(filename)
                else:
                    continue
    if not case:
        return False
    else:
        return case


def day_of_week(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    diena = int(datetime.datetime(year, month, day).strftime('%w'))
    if diena == 0 or diena == 6:
        return 0
    else:
        return 1


def get_case(c_case, i):
    get_case = []
    if i == 0:
        for f in range(len(c_case)):
            case = c_case[f]
            s = int((datetime.datetime.strptime(c_case[f][:8], "%Y%m%d")).strftime('%w'))
            if s == 0 or s == 6:
                get_case.append(case)
            else:
                continue
    else:
        for f in range(len(c_case)):
            case = c_case[f]
            s = int((datetime.datetime.strptime(c_case[f][:8], "%Y%m%d")).strftime('%w'))
            if 1 <= s <= 5:
                get_case.append(case)
            else:
                continue
    return get_case


year = input("Year: ")
month = input("Month: ")
day = input("Day: ")

case = year_case_finder(year, month, day)
if case == False:
    c_case = closest_case_finder(year, month, day)
    if c_case == False:
        print('No case exist!')
    else:
        i = day_of_week(year, month, day)
        case = get_case(c_case, i)
        print(case)
else:
    print('Exact case found, job done!')
    print(case)
