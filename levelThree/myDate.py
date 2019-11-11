import calendar
# print(time.asctime(time.localtime(time.time())))
day = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
a = input("Enter date : ")
a = a.split('-')
print(day[calendar.weekday(int(a[2]), int(a[1]), int(a[0]))])

