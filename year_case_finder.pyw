import os, datetime


def year_case_finder(year, month, day):
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
    diena = int(datetime.datetime(year, month, day).strftime('%w'))
    if diena == 0 or diena == 6:
        return 0
    else:
        return 1


 


def get_case_for_bd(c_case):
    bd_case =[]
    for f in range(len(c_case)):
        case = c_case[f]
        s = int((datetime.datetime.strptime(c_case[f][:8], "%Y%m%d")).strftime('%w'))
        if s == 0 or s == 6:
            bd_case.append(case)
        else:
            continue
    return bd_case


def get_case_for_dd(c_case):
    dd_case = []
    for f in range(len(c_case)):
        case = c_case[f]
        s = int((datetime.datetime.strptime(c_case[f][:8], "%Y%m%d")).strftime('%w'))
        if 1 <= s <= 5:
            dd_case.append(case)
        else:
            continue
    return dd_case


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


# if case == False:
#     c_case = closest_case_finder(year, month, day)
#     if c_case == False:
#         print('No case exist!')
#     else:
#         if day_of_week(year, month, day) == 0:  # brivdiena
#             case = get_case_for_bd(c_case)
#             print('Closest weekend day found, job done!')
#             print(case)
#         else:  # darba diena
#             case = get_case_for_dd(c_case)
#             print('Closest work day found, job done!')
#             print(case)
# else:
#     print('Exact case found, job done!')
#     print(case)