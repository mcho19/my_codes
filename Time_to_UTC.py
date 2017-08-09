import datetime
import pytz
from pytz import timezone



def time_convert():

    print('Which do you want to convert: \n'
          '1) US/Pacific to UTC \n'
          '2) UTC to US/Pacific \n')

    choice = int(raw_input())

    if choice == 1:
        tz = timezone('US/Pacific')
        utc = pytz.utc
        while True:

            print('Enter date in this format: mm/dd/yyyy (type quit to exit or return to select timezone) \n')
            date = raw_input()
            if date == 'quit':
                break
            date_converted = date.split('/')
            month, day, year = map(int, date_converted)
            if year <= 99:
                year = year + 2000


            print('Enter time in this format: hh:mm (type quit to exit)\n')
            time = raw_input()
            if time == 'quit':
                break
            time_converted = time.split(':')
            hours, minutes = map(int, time_converted)
            formatted_time = tz.localize(datetime.datetime(year, month, day, hours, minutes))
            converted_time = formatted_time.astimezone(utc)
            final_time = converted_time.strftime("%Y-%m-%d %H:%M")

            print('\nThis is the converted time/date in UTC: ' + str(final_time) + '\n')

    if choice == 2:
        tz = timezone('UTC')
        while True:

            print('Enter date in this format: mm/dd/yyyy (type quit to exit) \n')
            date = raw_input()
            if date == 'quit':
                break
            date_converted = date.split('/')
            month, day, year = map(int, date_converted)
            if year <= 99:
                year = year + 2000

            print('Enter time in this format: hh:mm (type quit to exit)\n')
            time = raw_input()
            if time == 'quit':
                break
            time_converted = time.split(':')
            hours, minutes = map(int, time_converted)
            formatted_time = tz.localize(datetime.datetime(year, month, day, hours, minutes))
            converted_time = formatted_time.astimezone(pytz.timezone('US/Pacific'))
            final_time = converted_time.strftime("%Y-%m-%d %H:%M")

            print('\nThis is the converted time/date in US/Pacific: ' + str(final_time) + '\n')

if __name__ == '__main__':
    time_convert()
