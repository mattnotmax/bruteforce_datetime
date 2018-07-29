#!/usr/bin/env python
'''
script to brute-force binary data looking for valid dates and times.

Currently supports Windows FILETIME

usage: ./bruteforce_dt.py <filename> <year to search in format 'YYYY'>
'''

__version__ = '0.2'

import struct
import os
from datetime import datetime, timedelta
import sys
import argparse

# Process commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest='file', help='Target Filename')
parser.add_argument(dest='year', help='year to search, format YYYY')
args = parser.parse_args()
file = args.file
if os.path.exists(file) == False:
    print('{} not found'.format(file))
    sys.exit()
year = args.year
# Basic data validation of YYYY between 1601 and 2042
while True:
    try:
        year = int(year)
    except ValueError:
        print('Error: check your command-line parameters. Should be ./bruteforce_dt.py <filename> YYYY')
        sys.exit()
    else:
        if year >= 1601 and year <= 2042:
            break
        else:
            print('Error: YYYY should be between 1601 and 2042')
            sys.exit()

def bruteforce_datetime(file, year):
    # open file, unpack 8 bytes starting from offset 0. Check if valid date and increment
    with open(file, 'rb') as file_open:
        filecontent = file_open.read()
        offset = 0
        date_dic = {}
        file_size = os.path.getsize(file)
        while offset <= (file_size - 8):
            possible_filetime = struct.unpack("<Q",filecontent[offset:(offset + 8)])[0]
            try:
                iso_datetime = datetime(1601,1,1) + timedelta(microseconds=(possible_filetime/10))
            except:
                pass
            iso_date = (str(iso_datetime))[0:19]
            if iso_date[0:4] == str(year):
                date_dic[offset] = iso_date # use dictionary of offset: date
            offset += 1
        if bool(date_dic) == False:
            print('There were no identified records matching the year {}'.format(year))
        else:
            print('Windows little-endian FILETIME records (in UTC) matching the year {} as follows:'.format(year))
            for key, value in sorted(date_dic.items()):
                print('Offset: {:#x}\tDate: {}'.format(key, value))

def main():
    print('bruteforce_dt.py: Test binary data for possible valid date/time formats. Version {}\n'.format(__version__))
    bruteforce_datetime(file, year)

if __name__== "__main__":
    main()
