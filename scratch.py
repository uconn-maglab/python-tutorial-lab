# starter = [1, 2, 45, "string", 12, 10, [1,2,3], 6, 33]
# good = []
#
# for n in starter:
#     try:
#         if n > 10:
#             good.append(n)
#         elif n == 10:
#             print("Fine, but it's supposed to be greater than 10.")
#             good.append(n)
#         else:
#             print(str(n) + " isn't greater than 10!")
#     except TypeError:
#         print("That's not even a number...")
#         continue
# print(good)
#
#
# def compare(a, b):
#     print("Comparing " + str(a) + " to " + str(b) + "...")
#     if a > b:
#         print(str(a) + " is bigger.")
#     elif a < b:
#         print(str(b) + " is bigger.")
#     else:
#         print("They're the same!")
#     print("\n")
#
# compare(1, 2)
# compare(5*2, 2*5)
# compare(555, 1)
#
#
# def compare_list(lst):
#     for pair in lst:
#         compare(pair[0], pair[1])
#
# pairs = [[1, 2], [5*2, 2*5], [555, 1]]
# compare_list(pairs)
#
#
# def compare(a, b):
#     while True:
#         try:
#             print("Comparing " + str(a) + " to " + str(b) + "...")
#             if a > b:
#                 print(str(a) + " is bigger.")
#             elif a < b:
#                 print(str(b) + " is bigger.")
#             else:
#                 print("They're the same!")
#             break
#         except ValueError:
#             print("Whoops those aren't numbers. String mode!")
#             a_len = len(a)
#             print(a + " is " + str(a_len) + " characters long.")
#             b_len = len(b)
#             print(b + " is " + str(b_len) + " characters long.")
#             if a_len > b_len:
#                 print(a + " is bigger.")
#             elif a_len < b_len:
#                 print(b + " is bigger.")
#             else:
#                 print("They're the same!")
#             break
#             # continue
#         except Exception:
#             print("I don't even know what to do with that input...")
#             break
#     print("\n")
#
# def compare_list(lst):
#     for pair in lst:
#         compare(pair[0], pair[1])
#
# pairs = [[1, 2], [5*2, 2*5], ["tiny", "huuuuuuuge"], [{"key":"value", "another_key":"another_value"}, 22], [555, 1]]
# compare_list(pairs)


class ComparisonError(Exception):
    """I don't even know what to do with that input..."""

def compare(a, b):
    # while True:
    try:
        if ((type(a) == "int") & (type(b) == "int")) | ((type(a) == "float") & (type(b) == "float")):
            print("Comparing " + str(a) + " to " + str(b) + "...")
            if a > b:
                print(str(a) + " is bigger.")
            elif a < b:
                print(str(b) + " is bigger.")
            else:
                print("They're the same!")
            # break
        elif (type(a) == "str") & (type(b) == "str"):
            print("Whoops those aren't numbers. String mode!")
            a_len = len(a)
            b_len = len(b)
            if a_len > b_len:
                print(a + " is bigger.")
            elif a_len < b_len:
                print(b + " is bigger.")
            else:
                print("They're the same!")
            # break
        else:
            raise ComparisonError
    except ComparisonError as e:
        print(e.__doc__)
        # pass
        # print("I don't even know what to do with that input...")
        # break

def compare_list(lst):
    for pair in lst:
        compare(pair[0], pair[1])

pairs = [[1, 2], [5*2, 2*5], ["tiny", "huuuuuuuge"], [{"key":"value", "another_key":"another_value"}, 22], [555, 1]]
compare_list(pairs)
