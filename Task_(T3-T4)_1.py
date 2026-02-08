from datetime import datetime

def get_days_from_today(date: str) -> int:    #Повернення цілого числа
    try:
        past_date = datetime.strptime(date, "%Y-%m-%d").date()    # Перетворення рядка в об'єкт дати
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'.")
        return None  # Повернення у разі помилки
    date_now = datetime.today().date()    # Отримання поточної дати
    diff_days = date_now - past_date    # Розрахунок кількості днів
    return diff_days.days    # Повернення кількості днів
print(f"Різниця між поточною і заданою датою: {get_days_from_today('2022-02-24')} днів")
