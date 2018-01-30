#! /usr/bin/python
import json
from pyntc import ntc_device as NTC

r1 = NTC(host='r1.aj.com', username='aj', password='cisco', secret='cisco', device_type='cisco_ios_ssh')

r2 = NTC(host='r2.aj.com', username='aj', password='cisco', secret='cisco', device_type='cisco_ios_ssh')

r3 = NTC(host='r3.aj.com', username='aj', password='cisco', secret='cisco', device_type='cisco_ios_ssh')

r4 = NTC(host='r4.aj.com', username='aj', password='cisco', secret='cisco', device_type='cisco_ios_ssh')

r5 = NTC(host='r5.aj.com', username='aj', password='cisco', secret='cisco', device_type='cisco_ios_ssh')

r6 = NTC(host='r6.aj.com', username='aj', password='cisco', secret='cisco', device_type='cisco_ios_ssh')

r7 = NTC(host='r7.aj.com', username='aj', password='cisco', secret='cisco', device_type='cisco_ios_ssh')

r1.reboot(confirm=True) 
