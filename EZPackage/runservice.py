import time
import pickle
from runservicemetadata.date import localtime
import random
import os
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen = 30
p =  "".join(random.sample(s,passlen ))

# SPLIT

print('Type your username.')
user = input('>')
if user.strip() == '':
    print('No New accounts detected, proceeding')
    time.sleep(1)
    print('Do you have any accounts you would like to load? (y/n)')
    yn = input('>')
    if yn.strip() == 'y':
        print('Accounts')
        print(user)
        print('Account #1')

# Split
with open('savefile.dat', 'wb') as f:
    pickle.dump([user], f, protocol=2)

with open('savefile.dat', 'rb') as f:
    user = pickle.load(f)


print('Do you have any accounts you would like to load? (y/n)')
yn = input('>')
if yn.strip() == 'y':
    print('Accounts')
    print(user)
    print('Account #1')
print('Open Logged. Opened at', localtime)
time.sleep(0.30)
print('Loading runservice..')
time.sleep(1)
print('EZLog')
time.sleep(0.60)
print('Loading Scripts..')
time.sleep(0.54)
print('EZexecutor')
time.sleep(1)
print('Generating Token')
time.sleep(3)
print('TOKEN= %s' % p)
time.sleep(1)
print('Starting session..')
time.sleep(3)
print('Logged in as%s' %user)
