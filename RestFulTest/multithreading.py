import threading


def cube(num):
    result = (num * num) * num
    print("Cube of the passed number is {}".format(result))


def square(num):
    result = (num * num)
    print("Square of the passed number is {}".format(result))


if __name__ == "__main__":
    t1 = threading.Thread(target=square, args=(10,))
    t2 = threading.Thread(target=cube, args=(20,))
    try:
        t1.start()
        t2.start()
        print(t1.getName())
        print(t2.getName())
        t1.join()
        t2.join()
    except TypeError:
        print("error is captured as {}")
        pass

    print("Threads are executed")
