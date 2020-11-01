import os
import sys
import time
from datetime import datetime as dt

from buildinfo import latest, pyv, version

d = dt.now()


# Initializing

print('You are currently running on version:')
print(version)
time.sleep(0.90)
print('Is Latest version?: %s' % latest)
time.sleep(1)
print('Python Version:%s' % pyv)
time.sleep(0.50)
if latest == 'y':
    print('You\'re all up to date!')
else:
    print('Updates required! Join the skittle\'s games discord server to get the most recent build.')
    quitsli = input('>')
    quit()
time.sleep(1)

animation = 'LOADING'

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
sanlength01 = 1920 
sanlength02 = 1080
sandboxcurrentsession = 0
init = 'True'
print("Loading Sequence complete.")
time.sleep(1)
print('Boonity Hub. Skittle 2020.')
print('Version%s' % version)
print('1. Installations')
print('2. My Games')
print('3. My discord Bots.')
print('4. BH info.')
m = input('>')
if m.strip() == '1':
    print('You have No current installations')
    print('Would you like to install some? {y/n}')
    i = input('>')
    if i.strip() == 'y':
        print('Name your price:')
        print('{P} Boonity Professional (23.99/m)')
        print('{C} Boonity Community edition (FREE)')
        b = input('>')
        if b.strip() == 'C':
            print('Community edition Chosen. Downloading Boonity Version 1.1.8 Setup file..')
            os.mkdir('BH Version 1.3')

elif m.strip() == '2':
    print('<My Games>')
    print('None')
    print('Current session shows you do not have any current games created, Would you like to create one?')
    c = input('>')
    if c.strip() == 'yes' or 'y':
    print('Downloading..')
    file = open("def.properties", 'w')
    file.write("Buildliscensed=True\nLiscenceID='908ad09a*DdWDwwn2uN'")
    file.close()
    time.sleep(1)
    file1 = open("modules.py", 'w')
    file.write
