from leapYear import isLeapYear

def validateDate(day, month, year):
    if month > 12 and month < 0:
        return False
    elif month in [1,3,5,7,8,10,12] and day < 32 and day > 0:
        return True
    elif month in [4,6,9,11] and day <= 30 and day > 0:
        return True
    elif month == 2 and day <= 28 and day > 0:
        return True
    elif isLeapYear(year) == True and month == 2 and day <= 29 and day > 0:
        return True
    return False



def main():
    day   = int(input("Gib ein Tag ein: "))
    month = int(input("Gib ein Monat ein: "))
    year  = int(input("Gib ein Jahr ein: "))
    print(validateDate(day, month, year))

if __name__ == "__main__":
    main()
