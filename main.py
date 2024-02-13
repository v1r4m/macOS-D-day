import rumps
from datetime import datetime, date
import schedule
import time

class DateApp(rumps.App):
    def __init__(self):
        super(DateApp, self).__init__("Date App")
        self.target_date = date(2024, 1, 30)
        self.update_date()

    def update_date(self):
        today = date.today()
        d_day = (today-self.target_date).days + 1
        self.title = f"{d_day}일"

if __name__ == "__main__":
    app = DateApp()

    # Schedule the update_date function to run every day at midnight
    schedule.every().day.at("00:00").do(app.update_date)

    app.run(background=True)

    # Keep the program running and check for scheduled tasks every second
    while True:
        schedule.run_pending()
        time.sleep(1)