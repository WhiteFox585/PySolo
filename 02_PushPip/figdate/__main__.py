import sys

from figdate.date import date

if len(sys.argv) == 1:
    date()
elif len(sys.argv) == 2:
    date(sys.argv[1])
elif len(sys.argv) == 3:
    date(sys.argv[1], sys.argv[2])
else:
    raise ValueError("ERROR! Wrong arguments count.")

