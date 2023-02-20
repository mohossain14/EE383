from datetime import date
from datetime import timedelta

today = date.today()
today_old = date.today() + timedelta(days = -30)

print("Today's date:", today)
print("Old date: ", today_old)