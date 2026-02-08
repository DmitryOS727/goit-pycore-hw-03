from datetime import datetime

def get_days_from_today(date: str) -> int:    #Повернення цілого числа
    
    past_date = datetime.strptime(date, "%d-%m-%Y")    # Перетворення рядка в об'єкт datetime
    date_now = datetime.today()    # Отримання поточної дати
    return date_now.toordinal() - past_date.toordinal()    # Розрахунок кількості днів
print(f"Різниця між поточним часом і заданою датою: {get_days_from_today('24-02-2022')} днів")


