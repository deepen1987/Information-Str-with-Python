"""
CS521 - A2
Deependrasingh Shekhawat

Script for calculating US census for next 5 years
"""

current_population = 312032486
max_years = [1, 2, 3, 4, 5]

print(f"US current population is {current_population} below is next 5 year forecast")

# calculating and printing population by year
for year in max_years:
    birth = (year * 365 * 24 * 60 * 60) // 7
    death = (year * 365 * 24 * 60 * 60) // 13
    new_imm = (year * 365 * 24 * 60 * 60) // 45
    future_population = current_population + birth + new_imm - death
    print(f"""
{year} year population {future_population}
    """)
