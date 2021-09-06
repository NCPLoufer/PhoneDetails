#!/usr/bin/python3

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = input('Enter the country code number and the number you want to find details for: ')

Country = phonenumbers.parse(number, 'Country')
print('The phone number is from:', geocoder.description_for_number(Country, 'en'))

ServProv = phonenumbers.parse(number, 'ServProv')
print('The Service Provider is:', carrier.name_for_number(ServProv, 'en'))

TimeZone = phonenumbers.parse(number, 'TimeZone')
print('TimeZone:', timezone.time_zones_for_number(TimeZone))
