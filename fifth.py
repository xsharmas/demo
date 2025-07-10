#write a code to print leap years from 2000 to 2024
def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def leap_years(start, end):
    """Generate a list of leap years between start and end (inclusive)."""
    return [year for year in range(start, end + 1) if is_leap_year(year)]
def main():
    start_year = 2000
    end_year = 2024
    leap_year_list = leap_years(start_year, end_year)
    print(f"Leap years from {start_year} to {end_year}: {leap_year_list}")
if __name__ == "__main__":
    main()
    print("Leap years generated successfully.")
# This code generates a list of leap years from 2000 to 2024
# using a simple function to check leap years and prints them.