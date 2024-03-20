import time
import random

fans = {1: 'отключено', 2: 'отключено', 3: 'отключено', 4: 'отключено'}

def f():
    global fans
    pumps = random.randint(0, 3)
    for i in range(1, len(fans) + 1):
        fans[i] = 'отключено'
    
    match pumps:
        case 0:
            print('вентиляторы и насосы отключены отключены')
            print(fans)
        case 1:
            for i in range(1, len(fans) - 1):
                fans[i] = 'включено'
            print('Работает 1 насос и 2 вентилятора')
            print(fans)
        case 2:
            for i in range(1, len(fans)):
                fans[i] = 'включено'
            print('Работает 2 насоса и 3 вентилятора')
            print(fans)
        case 3:
            for i in range(1, len(fans) + 1):
                fans[i] = 'включено'
            print('Работает более 2 насосов и 4 вентилятора')
            print(fans)

while True:
    time.sleep(1)
    f()