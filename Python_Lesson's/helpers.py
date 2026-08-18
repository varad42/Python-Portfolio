def shout(text):
    return text.upper() + "!!!"

def is_even(number):
    return number % 2 == 0

def greet(name):
    print("Hiii " + name)

if __name__ == "__main__":
    print(__name__)
    print("testing:", shout("hello"))