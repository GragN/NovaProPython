import time

pressure = 0
valve = 'положение задвижки'

def f():
    global pressure, valve
    if pressure < 1:
        valve = 'закрыта'
        pressure += 0.3
        print(f'давление {pressure} МПа, задвижка {valve}')
    elif pressure > 1 and pressure < 2:
        valve = 'положение 50%'
        pressure += 0.3
        print(f'давление {pressure} МПа, задвижка {valve}')
    elif pressure > 2 and pressure < 5:
        valve = 'открыта'
        pressure += 0.3
        print(f'давление {pressure} МПа, задвижка {valve}')
    else:
        pressure = 0
        valve = 'закрыта'
        print(f'сброс давления, задвижка {valve}')

while True:
    time.sleep(1)
    f()