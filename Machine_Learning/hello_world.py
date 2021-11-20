
class HelloWorld:

    def __init__(self):
        pass

    def print(self, msg):
        if msg:
            print(msg)
        else:
            print("Hello World")


if __name__ == '__main__':
    h = HelloWorld()
    h.print("")
