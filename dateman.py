""" Does date calculations based on requirements """

from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

import pprint
import sys

import api


def every_sun_2018():
    start = datetime(2017, 12, 30)
    end = datetime(2018, 12, 31)
    day = SU

    dates = list(rrule(WEEKLY, dtstart=start, until=end, byweekday=day))

    timestamps = []
    for dt in dates:
        timestamps.append(str(dt.timestamp()*1000)[0:13])

    return timestamps


def every_mon_wed_fri_2018():
    start = datetime(2017, 12, 30)
    end = datetime(2018, 12, 31)
    day = (MO, WE, FR)

    dates = list(rrule(DAILY, dtstart=start, until=end, byweekday=day))

    timestamps = []
    for dt in dates:
        timestamps.append(str(dt.timestamp()*1000)[0:13])

    return timestamps


def every_tue_th_sat_2018():
    start = datetime(2017, 12, 30)
    end = datetime(2018, 12, 31)
    day = (TU, TH, SA)

    dates = list(rrule(DAILY, dtstart=start, until=end, byweekday=day))

    timestamps = []
    for dt in dates:
        timestamps.append(str(dt.timestamp()*1000)[0:13])

    return timestamps


def every_wed_sat_sun_2018():
    start = datetime(2018, 1, 1)
    end = datetime(2018, 12, 31)
    day = (WE, SA, SU)

    dates = list(rrule(DAILY, dtstart=start, until=end, byweekday=day))

    timestamps = []
    for dt in dates:
        timestamps.append(str(dt.timestamp()*1000)[0:13])

    return timestamps

cu = api.ClickUp('token')

#print(cu.get_proj(603365))



alter = every_wed_sat_sun_2018()

for count, alt in enumerate(alter):
    cu.create_task(<List ID>, str(count+1), due=alt)

