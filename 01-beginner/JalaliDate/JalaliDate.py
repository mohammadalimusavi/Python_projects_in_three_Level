from persiantools.jdatetime import JalaliDate

year = int(input("ENTER YEAR: "))
month = int(input("ENTER MONTH: "))
day = int(input("ENTER DAY: "))

jalali_date = JalaliDate(year, month, day)
print(jalali_date.to_gregorian())

