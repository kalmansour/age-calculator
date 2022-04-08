from datetime import date
import datetime
from datetime import timedelta


def get_dob():
	birth_year = int(input("Enter birth year:"))
	birth_month = int(input("Enter birth month:"))
	birth_day = int(input("Enter birth day:"))
	dob = datetime.date(birth_year, birth_month, birth_day)
	return dob
	...


def get_age(dob):
	dob_year = dob.year
	today = date.today().year
	age = today - dob_year
	return age
	...


def main():
	dob = get_dob()
	today = date.today()
	
	if dob > today:
		print("Date of birth is invalid")
	else:
		age = get_age(dob)
		print("Age =", age)
	
	...


if __name__ == '__main__':
    main()
