from aocd import data
import re
import numpy as np
import pandas as pd
from datetime import datetime

dl = data.split('\n')


def create_timeseries(data):
    # Create the Dataframe
    pattern = re.compile(r'\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] (?P<action>.+)')
    actions = pd.Series(data)   # load into series
    df = actions.str.extract(pattern, expand=True)  # Expand via regex pattern
    
    # Create the timeseries index
    df[['year','month','day','hour','minute']] = df[['year','month','day','hour','minute']].apply(pd.to_numeric)  # Convert to int
    df[['year']] = 2018  # Forcing in-bounds year https://pandas-docs.github.io/pandas-docs-travis/timeseries.html#timeseries-oob
    df['ts'] = df.apply(lambda r: datetime(r.year, r.month, r.day, r.hour, r.minute, 0, 0), axis=1)  # Create timestamp field
    df['ts'] = pd.to_datetime(df.ts)  # Cast to pandas datetime
    df.drop(columns=['year','month','day', 'hour', 'minute'], inplace=True)  # Don't need these anymore
    df.set_index('ts', inplace=True)
    
    # Pull out guard id and set asleep flag
    guard_regex_pattern = re.compile(r'Guard #(?P<guard_id>\d+) begins shift')
    df['guard_id'] = df['action'].str.extract(guard_regex_pattern, expand=True)  # Pull out guard id
    df['asleep'] = np.where(df['action'] == 'falls asleep', 1, 0)

    # Fill empty timeslots so we have every minute to work with and filldown
    idx = pd.date_range(start=min(df.index), end=max(df.index), freq='min')
    idx = idx[(idx.hour == 0) | (idx.hour == 23)]  # Add entries for each minute during the midnight hour and before when they click in
    df = df.reindex(idx)
    df.sort_index(inplace=True)

    df['asleep'].ffill(inplace=True)  # filldown asleep flag
    df['guard_id'].ffill(inplace=True)  # Fill down guard id
    df['minute'] = df.index.minute
    return df

def part_a(data):
    df = create_timeseries(data)
    
    # Group by guard and minute and add them
    guard_sum = df.groupby(['guard_id']).sum()
    guard_num = guard_sum.idxmax().asleep # Sleepiest guard

    # Get guard schedule
    minute_sum = df[df['guard_id'] == guard_num].groupby('minute').sum()
    min_num = minute_sum.idxmax().asleep  # Sleepiest minute

    return int(guard_num) * int(min_num)


def part_b(data):
    df = create_timeseries(data)

    # Group by guard_id and minute
    sleepiest_guard_min = df.groupby(['guard_id','minute']).sum()
    i = sleepiest_guard_min.idxmax()
    return int(i.asleep[0]) * int(i.asleep[1])

ex1 = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up']

assert part_a(ex1) == 240
print("A: {}".format(part_a(dl)))

assert part_b(ex1) == 4455
print("B: {}".format(part_b(dl)))