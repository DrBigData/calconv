#!/usr/bin/python3

#
# Convert between the Gregorian Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

epoch = 1480366

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive dates
        y = 1
        cycles = (year - y) // 400
        y += (400 * cycles)
        jday += (cycles * cycle400)
        while y < year:
            if year - y > 400:
                y += 400
                jday += cycle400
            elif year - y > 100:
                y += 100
                jday += cycle100
            elif year - y > 4:
                y += 4
                jday += cycle4
            elif y % 400 == 260:
                y += 1
                jday += 366
            elif y % 100 == 60:
                y += 1
                jday += 365
            elif y % 4 == 0:
                y += 1
                jday += 366
            else:
                y += 1
                jday += 365

        if year % 400 == 260:
            m = months.JAPANESE_LEAP
        elif year % 100 == 60:
            m = months.JAPANESE_NORMAL
        elif year % 4 == 0:
            m = months.JAPANESE_LEAP
        else:
            m = months.JAPANESE_NORMAL
    else:
        # negative years
        y = 0
        cycles = (y - year) // 400
        y -= (400 * cycles)
        jday -= (cycles * cycle400)
        
        while y > year:
            if y - year > 400:
                y -= 400
                jday -= cycle400
            else:
                y -= 1
                if abs(y) % 400 == 141:
                    jday -= 366
                elif abs(y) % 100 == 41:
                    jday -= 365
                elif abs(y) % 4 == 1:
                    jday -= 366
                else:
                    jday -= 365

        if abs(year) % 400 == 141:
            m = months.JAPANESE_LEAP
        elif abs(year) % 100 == 41:
            m = months.JAPANESE_NORMAL
        elif abs(year) % 4 == 1:
            m = months.JAPANESE_LEAP
        else:
            m = months.JAPANESE_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Gregorian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    ganjitsu = epoch
    curryear = False

    if jday >= epoch:
        # positive date
        year = 1
        cycles = (jday - ganjitsu) // cycle400
        year += (400 * cycles)
        ganjitsu += (cycles * cycle400)
        while curryear == False:
            if jday - ganjitsu > cycle400:
                year += 400
                ganjitsu += cycle400
            else:
                #year += 1
                if year % 400 == 260:
                    if jday - ganjitsu < 366:
                        curryear = True
                    else:
                        ganjitsu += 366
                        year += 1
                elif year % 100 == 60:
                    if jday - ganjitsu < 365:
                        curryear = True
                    else:
                        ganjitsu += 365
                        year += 1
                elif year % 4 == 0:
                    if jday - ganjitsu < 366:
                        curryear = True
                    else:
                        ganjitsu += 366
                        year += 1
                else:
                    if jday - ganjitsu < 365:
                        curryear = True
                    else:
                        ganjitsu += 365
                        year +=1
        
        if year % 400 == 260:
            # leap year
            m = months.JAPANESE_LEAP
        elif year % 100 == 60:
            # not a leap year
            m = months.JAPANESE_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.JAPANESE_LEAP
        else:
            # not a leap year
            m = months.JAPANESE_NORMAL

    else:
        # negative date
        cycles = (ganjitsu - jday) // cycle400
        year -= (400 * cycles)
        ganjitsu -= (cycles * cycle400)

        while ganjitsu > jday:
            year -= 1
            if abs(year) % 400 == 141:
                ganjitsu -= 366
            elif abs(year) % 100 == 41:
                ganjitsu -= 365
            elif abs(year) % 4 == 1:
                ganjitsu -= 366
            else:
                ganjitsu -= 365
           
        if abs(year) % 400 == 141:
            # leap year
            m = months.JAPANESE_LEAP
        elif abs(year) % 100 == 41:
            # not a leap year
            m = months.JAPANESE_NORMAL
        elif abs(year) % 4 == 1:
            # leap year
            m = months.JAPANESE_LEAP
        else:
            # not leap year
            m = months.JAPANESE_NORMAL

    delta = jday - ganjitsu
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
