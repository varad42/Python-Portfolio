
# Lesson 25: Inheritance — classes built on classes 🧬


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


