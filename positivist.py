#!/usr/bin/python

#
# Convert between Positivist calendar and Julian day
#

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

def tojd(day, month, year):

    day = int(day)
    month = month
    year = int(year)
    days = 0

    if year >= 0:
        alpha = 2374112
        for y in range(0, year):
            if y % 400 == 0:
                days += 366
            elif y % 100 == 0:
                days += 365
            elif y % 4 == 0:
                days += 366
            else:
                days += 365
        
        if year % 400 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.POSITIVIST_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        else:
            # not a leap year
            m = months.POSITIVIST_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        alpha = 2374113
        year = 0 - year

        for y in range(0, year):
            if y % 400 == 0:
                days -= 366
            elif y % 100 == 0:
                days -= 365
            elif y % 4 == 0:
                days -= 366
            else:
                days -= 365        

        if year % 400 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.POSITIVIST_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        else:
            # not a leap year
            m = months.POSITIVIST_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Positivist calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 2374112:
        # positive date
        delta = jday - 2374112
        current = False

        while delta > cycle400:
            year += 400
            delta -= cycle400

        while delta > cycle100:
            year += 100
            delta -= cycle100

        while delta > cycle4:
            year += 4
            delta -= cycle4

        while current == False:
            if year % 400 == 0:
                if delta <= 366:
                    current = True
                    break
                else:
                    delta -= 366
            elif year % 100 == 0:
                if delta <= 365:
                    current = True
                    break
                else:
                    delta -= 365
            elif year % 4 == 0:
                if delta <= 366:
                    current = True
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                    break
                else:
                    delta -= 365
            year += 1

        if year % 400 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.POSITIVIST_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        else:
            # not a leap year
            m = months.POSITIVIST_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 2374113 - jday
        current = False

        while delta > 0:
            if abs(year) % 400 == 0:
                delta -= 366
            elif abs(year) % 100 == 0:
                delta -= 365
            elif abs(year) % 4 == 0:
                delta -= 366
            else:
                delta -= 365
            year -= 1

        delta = 0 - delta

        if delta == 0:
            year -= 1
            if abs(year) % 400 == 0:
                delta = 366
            elif abs(year) % 100 == 0:
                delta = 365
            elif abs(year) % 4 == 0:
                delta = 366
            else:
                delta = 365
                
        if abs(year) % 400 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        elif abs(year) % 100 == 0:
            # not a leap year
            m = months.POSITIVIST_NORMAL
        elif abs(year) % 4 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        else:
            # not leap year
            m = months.POSITIVIST_NORMAL


        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)
