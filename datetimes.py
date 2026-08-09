from datetime import datetime,timedelta

current=datetime.today()



now=current.time()
today_date=current.date()
past_date = datetime.strptime("2026-06-21","%Y-%m-%d").date()

Time= current.strftime("%H:%M:%S")
Date=current.strftime("%d/%B/%Y")


days_between = (today_date - past_date).days


current_time = datetime.today().time()
final_time = current_time.strftime("%H_%M_%S")

yesterday = today_date - timedelta(days=1)
print(yesterday)