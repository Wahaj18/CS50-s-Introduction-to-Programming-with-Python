from datetime import date
import sys
import inflect

def main():
    p = inflect.engine()
    date_today = date.today()
    date_birth = get_date(input("Date of Birth: "))
    minutes = get_minutes(date_today, date_birth)
    m = p.number_to_words(minutes, andword='').capitalize()
    print(f"{m} minutes")

def get_minutes(date_today, date_birth):
    diff = date_today - date_birth
    return round(diff.total_seconds() / 60)

def get_date(d):
    try:
        date_birth = date.fromisoformat(d)
    except (ValueError,TypeError):
        sys.exit("Invalid Date")
    return date_birth

if __name__ == "__main__":
    main()
