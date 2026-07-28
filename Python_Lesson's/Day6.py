# tasks_done = {"run", "study"}
# tasks_all = {"run", "study", "eat", "sleep"}
#
# print(tasks_all - tasks_done)      # {'eat', 'sleep'} — set MATH: what remains!

# fav_num = (0,1,2)
# print(fav_num[1])
# fav_num[0] = 5
# print(fav_num)

# num = [1, 2, 2, 3, 3, 3, 4]
# num_set = list(set(num))
# print(num_set)

# my_hobbies = {"dance","music","cricket","football"}
# friend_hobbies = {"dance","music","batminton","reading"}
# print(my_hobbies | friend_hobbies)
# print(my_hobbies & friend_hobbies)
# print(my_hobbies - friend_hobbies)



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

#
# class UrgentTask(Task):                    # ← the parentheses: "I'm a Task, plus extras"
#     def display(self):
#         return "🔥 " + self.name + " (URGENT!)"
#
# u = UrgentTask("pay bill")     # __init__?? UrgentTask has none... uses TASK's! name, done — all there
# u.complete()                   # complete?? not defined here either — INHERITED, works
# print(u.display())             # 🔥 pay bill (URGENT!) — the OVERRIDE wins
#
# todos.append(UrgentTask("pay bill"))    # slots into your Task list perfectly
# for t in todos:
#     print(t.display())                  # each object answers with ITS OWN display!







# l = LazyTask("nap")
# print(l.display())
#
# u = UrgentTask("pay bill", "Friday")
# print(u.to_dict())
#
#
#
#
# u = UrgentTask("varad", "Friday")
# print(u.display())         # 🔥 pay bill (by Friday)
# u.complete()
# print(u.done)              # True — inherited machinery still intact

# t = Task("study")
# u = UrgentTask("pay bill")
#
# print(t.display())
# print(u.display())
#
# both = [t, u]                 # ONE list holding BOTH kinds
# for item in both:
#     print(item.display())     # ONE line of code...
#
# u.complete()
# print(u.done)        # True — but WHERE did complete() come from? You never wrote it in UrgentTask!


