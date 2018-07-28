# bruteforce_datetime

script to brute-force binary data looking for valid dates and times.

Currently supports Windows FILETIME

usage: ./brutus.py <filename> <year to search in format 'YYYY'>
  
Requirements: Python 3.x

Sample output:

$ python3 ./brutus.py single_event_carved.bin 2018
Possible Windows little-endian FILETIME records matching the year 2018 as follows:
Offset: 0x10    Date: 2018-03-18 11:15:00
Offset: 0x82    Date: 2018-03-18 11:15:00
Offset: 0x92    Date: 2018-03-07 08:43:03
Offset: 0x93    Date: 2018-03-07 08:43:03

NB: All records presented in UTC

