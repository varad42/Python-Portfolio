# Lesson 24: Function power-ups 🔋

# tasks_done = {"run", "study"}
# tasks_all = {"run", "study", "eat", "sleep"}
#
# print(tasks_all - tasks_done)      # {'eat', 'sleep'} — set MATH: what remains!





# s = {Task("run"), Task("run")}

# def order_chai(sugar="normal"):
#     return "One chai, sugar: " + sugar
#
# print(order_chai())
# print(order_chai("extra"))
#
# def intro(name, age):
#     return name + " is " + str(age)
#
# print(intro(age=21, name="Varad"))
#
# def show_all(*things):
#     print(things)             # peek at the tuple itself!
#
# show_all(1, 2)
# show_all("a", "b", "c")
# show_all()



# def power(base, exponent=2):
#     return base**exponent
#
# print(power(5))
# print(power(2,10))

def longest(*words):
    best = []                    # best-so-far box
    for w in words:
        if len(best) < len(w) :                  # is this one longer than the current best?
            best = w
    return best

print(longest("i","will","win","the","game"))

def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"

print(greet(greeting="Yo", name="Varad"))