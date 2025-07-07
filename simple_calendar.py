
calendar_data = {}

days_in_month = 31
first_day_weekday = 1 
def display_month():
    """Display a simple calendar for July 2025."""
    print("\nCalendar for July 2025")
    print("Mo Tu We Th Fr Sa Su")
    

    print("   " * first_day_weekday, end="")

    current_weekday = first_day_weekday
    
    for day in range(1, days_in_month + 1):
        date_str = f"2025-07-{day:02d}"
        if date_str in calendar_data and calendar_data[date_str]:
            print(f"*{day:2d}", end=" ")
        else:
            print(f" {day:2d}", end=" ")
        
        current_weekday += 1
        if current_weekday % 7 == 0:
            print()

def main():
    display_month()

if __name__ == "__main__":
    main()