import rumps
from datetime import datetime, date
import schedule
import time

class DateApp(rumps.App):
    def __init__(self):
        super(DateApp, self).__init__("Date App")
        self.target_date = date.today()  # default target date
        self.update_date()

    @rumps.clicked("Set Target Date")
    def set_target_date(self, _):
        window = rumps.Window(message='Enter target date in YYYY-MM-DD format', 
                              title='Set Target Date', 
                              default_text=str(self.target_date),
                              dimensions=(300, 24))
        response = window.run()
        if response.clicked:
            self.target_date = datetime.strptime(response.text, '%Y-%m-%d').date()
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