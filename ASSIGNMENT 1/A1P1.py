years = int(input("Enter total number of years: "))

print(f"In {years} years there are: ")
print(f"No. of days: {years * 365} days")
print(f"No. of hours: {years * 365 * 24} hours")
print(f"No. of minutes: {years * 365 * 24 * 60} minutes")
print(f"No. of seconds: {years * 365 * 24 * 60 * 60} seconds")


year = int(input("Enter the year: "))

if (year % 4 == 0):
    if (year % 100 == 0) :
        if (year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is  a leap year")
else:
    print(f"{year} is not a leap year")