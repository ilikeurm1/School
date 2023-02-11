# https://dodona.ugent.be/en/courses/1575/series/17297/activities/1800551125/

# ---> Imports <---

from datetime import datetime

# ---> Variables <---

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

"""
lente	21 maart	    20 juni
zomer	21 juni	        22 september
herfst	23 september	20 december
winter	21 december	    20 maart
"""
leapYear = 2020 # 29 Feb is tested, so must be leap year
startWinter = datetime(leapYear, 12, 21)
startFall = datetime(leapYear, 9, 23)
startSummer = datetime(leapYear, 6, 21)
startSpring = datetime(leapYear, 3, 21)

# ---> Inputs <---
Day = int(input('Which day is it: '))
Month = input('Which month is it: ')
indexM = Months.index(Month)

try: 
    # ---> Calculations <---
    myDate = datetime(leapYear, indexM + 1, Day)
    Worked = True
    if (myDate >= startWinter or myDate < startSpring):
        Season='winter' # winter
    elif (myDate >= startSpring and myDate < startSummer):
        Season='spring' # spring
    elif (myDate >= startSummer and myDate < startFall):
        Season='summer' # summer
    else:
        Season = 'autumn' # autumn
        
    print(f'It is {Season} on {Month} {Day}.')

except ValueError:
    Worked = False
    print(Worked)
