
def get_period(hour):
    if 0 <= hour <= 5:
        return "ночь"
    elif 6 <= hour <= 11:
        return "утро"
    elif 12 <= hour <= 17:
        return "день"
    elif 18 <= hour <= 23:
        return "вечер"
    else:
        return "некорректное значение"



hour = int(input())
time_of_day = get_period(hour)
print(time_of_day)
