x = int(input('x: '))
y = int(input('y: '))

try:
    result = x / y
except ZeroDivisionError:
    print('Error: Cannot devide by 0.')

print(f"{x} / {y} = {result}")