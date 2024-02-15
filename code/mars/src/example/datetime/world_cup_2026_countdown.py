# world_cup_2026_countdown.py

from dateutil import parser, tz
from dateutil.relativedelta import relativedelta
from datetime import datetime

# World Cup 2026 June 11 – July 19 2026
WORLD_CUP_2026_DATE = parser.parse("Jun 11, 2026 10:00 AM")
WORLD_CUP_2026_DATE = WORLD_CUP_2026_DATE.replace(tzinfo=tz.gettz("America/New_York"))
now = datetime.now(tz=tz.tzlocal())

# Countdown to World Cup 2026: relativedelta(years=+5, months=+5, days=+6, hours=+13, minutes=+59, seconds=+59, microseconds=+999999)
countdown = relativedelta(WORLD_CUP_2026_DATE, now)
print(f"Countdown to World Cup 2026: {countdown}")

def time_amount(time_unit: str, countdown: relativedelta) -> str:
    """
    Args:
    time_unit (str): The time unit to be used in the countdown.
    countdown (relativedelta instance): The time difference between two dates.
    """
    t = getattr(countdown, time_unit)
    return f"{t} {time_unit}" if t != 0 else ""

def main():
    now = datetime.now(tz=tz.tzlocal())
    countdown = relativedelta(WORLD_CUP_2026_DATE, now)
    time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
    output = (t for tu in time_units if (t := time_amount(tu, countdown)))
    pycon_date_str = WORLD_CUP_2026_DATE.strftime("%A, %B %d, %Y at %H:%M %p %Z")
    print(f"World Cup 2026 will start on:", pycon_date_str)
    print("Countdown to World Cup 2026:", ", ".join(output))

#countdown = relativedelta(WORLD_CUP_2026_DATE, now)
#time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
#output = (t for tu in time_units if (t := time_amount(tu, countdown)))
#print("Countdown to World Cup 2026:", ", ".join(output))

# Guard clause to make sure that main() only runs when this file is executed as a script.
if __name__ == "__main__":
    main()