def is_leap_year(year):
   """Checks if a given year is a leap year.

  Args:
    year: An integer representing the year.

  Returns:
    True if the year is a leap year, False otherwise.
    """
   if(year %4 == 0 and year %100 !=0) or (year %400==0):
      return True
   
   else:
      return False
   
# Example usage:
year1 = 2024
year2 = 1900
year3 = 2000
year4 = 2023

print(f"{year1} is a leap year: {is_leap_year(year1)}")
print(f"{year2} is a leap year: {is_leap_year(year2)}")
print(f"{year3} is a leap year: {is_leap_year(year3)}")
print(f"{year4} is a leap year: {is_leap_year(year4)}")