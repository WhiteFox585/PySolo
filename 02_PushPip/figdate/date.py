import datetime
from pyfiglet import Figlet

def date(format="%Y %d %b, %A", font="graceful"):
    print(Figlet(font=font).renderText(datetime.date.today().strftime(format)))