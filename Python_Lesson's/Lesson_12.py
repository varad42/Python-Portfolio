# Lesson 12 preview: Loops + Dictionaries, the dream team
# marks = {"math": 95, "science": 88, "english": 76}
#
# for subject in marks:
#     print(subject + ": " + str(marks[subject]))
#
# print(marks.keys())     # all the labels
# print(marks.values())   # all the contents
#
# for subject, score in marks.items():
#     print(subject + ": " + str(score))


# marks = {"math": 75,"sci": 50,"geo": 90,"his": 100}
#
# for subject, score in marks.items():
#     print(subject + ": " + str(score))
#
# print(marks.keys())
# print(marks.values())
#
# for subject, score in marks.items():
#     if score >= 90:
#         print(subject + ": A")
#     elif score >= 75:
#         print(subject + ": B")
#     else:
#         print(subject + ": C")
#
# def total(dic):
#     total = 0
#     for subject, score in dic.items():
#         total += score
#     return total
#
#
# total_marks = total(marks)
# print(total({"art": 50}))
# print(total_marks)