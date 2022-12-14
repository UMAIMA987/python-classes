#==================print greetings according to time============

import time
timestamp = time.strftime('%H:%M:%S')
print("Time:", timestamp)

timestamp_1 = int(time.strftime('%H'))
print("Hour:", timestamp_1)

timestamp_2= int(time.strftime('%M'))
print("Minute:" , timestamp_2)

timestamp_3 = int(time.strftime('%S'))
print("Seconds:" , timestamp_3)


if timestamp_1> 6 and timestamp_1< 12:
    print("Good morning Sir")
elif timestamp_1 >=12 and timestamp_1<16:
    print("Good Afternoon")
elif timestamp_1 >=16 and timestamp_1<21:
    print("Good Evening")
else:
    print("Good Night")

