import math


def myabs(x):
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return None


# print(myabs(0))

def move(x, y, step, angle=math.pi / 6):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))

x, y = move(100, 100, 60)
print(x, y)


def ar(*args):
    print(args)
    # retrun args


print(ar(['a', 'b']))
# result = ar(['a', 'b'])
# print(result)
