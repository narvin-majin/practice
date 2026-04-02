def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year %4 == 0:
        return True
    else:
        return False
    
    #def is_leap(year):
    #return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input().strip())


#2026-04-01 | leap funcion hr | solved | 30min | edge case solved | narvin