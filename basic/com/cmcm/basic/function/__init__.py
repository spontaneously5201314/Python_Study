import math


def my_abs(num):
    if num > 0:
        return num
    elif num < 0:
        return -num
    else:
        return None


# print(my_abs(0))

def move(x, y, step, angle=math.pi / 6):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# print(type(move(100, 100, 60, math.pi / 6)))
# print(move(100, 100, 60, math.pi / 6))

x, y = move(100, 100, 60)


# print(x, y)


def ar(*args):
    print(args)
    # retrun args


# print(ar(['a', 'b']))
# result = ar(['a', 'b'])
# print(result)

result = [1, 2, 3]
# print(result.__slots__)
