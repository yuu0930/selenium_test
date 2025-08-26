def leap_year_check(year):
    if year % 4 != 0:
        print("うるう年ではありません")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("うるう年です")
    elif year % 4 == 0 and year % 100 == 0:
        print("うるう年ではありません")
    elif year % 4 == 0:
        print("うるう年です")

year = 1800
leap_year_check(year)


def leap_year_check2(year):
    if year % 400 == 0:
        print("閏年です")
    elif year % 100 == 0:
        print("閏年ではありません")
    elif year % 4 == 0:
        print("閏年です")
    else: 
        print("閏年ではありません")

year = 2024
leap_year_check2(year)