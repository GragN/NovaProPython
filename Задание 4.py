

def f(initial_value, difference, amount_of_elements):
    array = []
    sum = 0
    array.append(initial_value)
    for i in range(0, amount_of_elements):
        number = array[i] + difference
        array.append(number)
        sum += array[i]
    print(sum)

f(1, 1, 10)