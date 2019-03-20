month = input('type in month: ')
day = int(input('select a numerical day'))

x = ['January', 'February', 'March']
y = ['April', 'May', 'June']
z = ['July' 'August', 'September']

if month in (x):
    season = 'winter'
elif month in (y):
    season = 'spring'
elif month in (z):
    season = 'summer'
else:
    season = 'autumn'

if (month == 'March') and (day > 19):
    season = 'spring'
elif (month == 'June') and (day > 20):
    season == 'summer'
elif (month == 'September') and (day > 21):
    season == 'autumn'
elif (month == 'December') and (day > 20):
    season == 'winter'

print('Season is', season)


month = input('What is month of your birth: ')
day = int(input('What is numerical day of your birth'))

sign = 'Crap'

if month == 'December':
    sign = 'Saggitarius' if day < 22 else 'Capicorn'
elif month == 'January':
    sign = 'Capicorn' if day < 20 else 'Aquarius'
elif month == 'February':
    sign = 'Aquarius' if day < 19 else 'Pisces'
elif month == 'March':
    sign = 'Pisces' if day < 21 else 'Aries'
elif month == 'April':
    sign = 'Aries' if day < 20 else 'Taurus'
elif month == 'May':
    sign = 'Taurus' if day < 21 else 'Gemini'
elif month == 'June':
    sign = 'Gemini' if day < 21 else 'Cancer'
elif month == 'July':
    sign = 'Cancer' if day < 23 else 'Leo'
elif month == 'August':
    sign = 'Leo' if day < 23 else 'Virgo'
elif month == 'September':
    sign = 'Virgo' if day < 23 else 'Libra'
elif month == 'October':
    sign = 'Libra' if day < 23 else 'Scorpio'
elif month == 'November':
    sign = 'Scorpio' if day < 22 else 'Saggitarius'

print ('your sign from the stars is', sign)

a = float(input('first number: '))
b = float(input('second number: '))
c = float(input('third number: '))

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print('the median is: ', median)




