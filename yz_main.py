import rumps

import data

from datetime import datetime, date, timedelta

from frc_days import frc_days

foo = "bar"

class year_zero_app(object):
    def __init__(self):
        self.config = {
            "app_name": "year zero",
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 1)
        self.rev_calendar()
        # self.timer.start()
        

    def rev_calendar(self):
        # this creates a date object for the last day of the previous year
        year0 = date(date.today().year-1, 12, 31)
        # this creates a date object for the last day of the current year
        year1 = date(date.today().year  , 12, 31)

        # this calculates the year length in days
        year_len = (year1 - year0).days

        # this caluclates the offset between a date in gregorian vs revolutionary
        offset = (year1 - date(date.today().year, 9, 22)).days

        # this calculates the number of days so far in this year
        today = (date.today() - year0)

        # this then converts that into the number of days so far in the FRC
        rev_today = (today.days + offset) % year_len

        self.day_name = frc_days[rev_today]

        if rev_today > 30:
            self.day_no = (rev_today % 30) + 1

        if 0 < rev_today <= 30:
            self.month = "Vendémiaire"

        if 30 < rev_today <= 60:
            self.month = "Brumaire"

        if 60 < rev_today <= 90:
            self.month = "Frimaire"

        if 90 < rev_today <= 120:
            self.month = "Nivôse"

        if 120 < rev_today <= 150:
            self.month = "Pluviôse"

        if 150 < rev_today <= 180:
            self.month = "Ventôse"

        if 180 < rev_today <= 210:
            self.month = "Germinal"

        if 210 < rev_today <= 240:
            self.month = "Floréal"

        if 240 < rev_today <= 270:
            self.month = "Prairial"

        if 270 < rev_today <= 300:
            self.month = "Messidor"

        if 300 < rev_today <= 330:
            self.month = "Thermidor"

        if 330 < rev_today <= 360:
            self.month = "Fructidor"

        if 360 < rev_today <= 366:
            self.month = "Sansculottides"

        self.app.title = f"{self.day_name} {self.day_no} {self.month}"    



    def on_tick(self, sender):
        now = datetime.today()
        total_sec = 0
        total_sec += now.hour * 60 * 60
        total_sec += now.minute * 60
        total_sec += now.second

        total_rev_sec = round(total_sec / 0.864)

        cur_rev_hour = int(total_rev_sec // 10000)
        total_rev_sec = total_rev_sec % 10000

        cur_rev_min = int(total_rev_sec // 100)
        total_rev_sec = total_rev_sec % 100

        cur_rev_sec = total_rev_sec

        self.app.title = f"{cur_rev_hour}:{cur_rev_min:0>2d}" # :{round(cur_rev_sec):0>2d}"


    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = year_zero_app()
    app.run()