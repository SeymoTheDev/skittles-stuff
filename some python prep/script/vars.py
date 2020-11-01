import time
import sys


print('Would you like to initialize loading sequence? {y/n}')

c = input('>')
if c.strip() == 'y':
    print('Initializing Loading Sequence...')

elif c.strip() == 'n':
    quit()
# some Loading Biz
animation = "|/-\\"

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
a=10
b=20
c=40
d=93
e=32
isnewsession=1
print("Loading Sequence complete.")


