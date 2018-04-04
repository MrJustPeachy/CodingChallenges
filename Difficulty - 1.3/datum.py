data = [int(n) for n in input().strip().split()]

day = data[0]
month = data[1]

thursday = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
friday = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
saturday = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sunday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
monday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
tuesday = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
wednesday = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']

if month == 1:
    dayPos = (day % 7) - 1
    print(thursday[dayPos])

elif month == 2:
    dayPos = (day % 7) - 1
    print(sunday[dayPos])

elif month == 3:
    dayPos = (day % 7) - 1
    print(sunday[dayPos])

elif month == 4:
    dayPos = (day % 7) - 1
    print(wednesday[dayPos])

elif month == 5:
    dayPos = (day % 7) - 1
    print(friday[dayPos])

elif month == 6:
    dayPos = (day % 7) - 1
    print(monday[dayPos])

elif month == 7:
    dayPos = (day % 7) - 1
    print(wednesday[dayPos])

elif month == 8:
    dayPos = (day % 7) - 1
    print(saturday[dayPos])

elif month == 9:
    dayPos = (day % 7) - 1
    print(tuesday[dayPos])

elif month == 10:
    dayPos = (day % 7) - 1
    print(thursday[dayPos])

elif month == 11:
    dayPos = (day % 7) - 1
    print(sunday[dayPos])

else:
    dayPos = (day % 7) - 1
    print(tuesday[dayPos])

