"""generator as param of func"""

# coding = utf8


def inner_generator():
    for i in range(10):
        yield i


def outer_generator(inner_generator):
    for i in inner_generator:
        yield i * 2


if __name__ == '__main__':
    ig = inner_generator()
    for i, v in enumerate(outer_generator(ig)):
        print(i, v)
        if i == 4:
            break
    for i, v in enumerate(outer_generator(inner_generator())):
        print(i, v)
    for i, v in enumerate(outer_generator(ig)):
        print(i, v)
