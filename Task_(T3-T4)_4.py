from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        bday_this_year = bday.replace(year=today.year)    # Поставити день народження в поточний рік

        # якщо ДР вже був в цьому році, то поставити його на наступний рік
        if bday_this_year < today:
            bday_this_year = bday_this_year.replace(year=today.year + 1)

        #   перевіряємо, чи ДР в цьому році буде в найближчі 7 днів
        if (bday_this_year - today).days >= 0 and (bday_this_year - today).days <= 7:
            congratulation_date = bday_this_year

        # якщо вихідні
        if congratulation_date.weekday() == 5:
            congratulation_date = congratulation_date + timedelta(days=2)

        if congratulation_date.weekday() == 6:
            congratulation_date = congratulation_date + timedelta(days=1)

        result.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
        })

    return result

# приклад
users = [
    {"name": "John Doe", "birthday": "1985.02.09"},
    {"name": "Jane Smith", "birthday": "1990.07.12"},
    {"name": "Petro Kuk", "birthday": "1975.02.09"},
    {"name": "Helen Pods", "birthday": "1991.03.12"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)