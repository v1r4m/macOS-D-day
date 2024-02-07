import rumps
from datetime import datetime, date

class DateApp(rumps.App):
    def __init__(self):
        super(DateApp, self).__init__("Date App")

    @rumps.timer(60)  # every 60 seconds the function will be called
    def update_date(self, _):
        target_date = date(2024, 1, 30)
        today = date.today()
        d_day = (today-target_date).days + 1
        self.title = f"{d_day}일"

if __name__ == "__main__":
    DateApp().run()