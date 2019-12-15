# def dzielenie(a,b):
#     return a/b
#
# print(dzielenie(4,2)== 2) # Sprawdzamy od razu odpowiedż

# if dzielenie(4,2)== 2:
#     print("Passed")
# else:
#     raise Exception("failed")
#
# if dzielenie(5,10)== 0.5:
#     print("Passed")
# else:
#     raise Exception("failed")

### ALBO!

# assert dzielenie(10,5) == 4, "Failed"

#
# def suma(a,b):
#     return (a+b)**2
#
# assert suma(1, 1) == 4, "failed"
# assert suma(0, 0) == 0, "failed"
# assert suma(1.5, 1.5) == 9, "failed"

# Asercje nie służą tylko do testowania

#
# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("nie można dzielić przzez 0")
# div(5,0)

#ALBO
# def div(a,b):
#     assert b != 0, "nie można dzielić przez 0"
#     return a/b
#
# div(5,0)


def konkatenacja(str1, str2):
    return str1 + str2

assert konkatenacja("asd", "fgh") == "asdfgh", "failed"
assert konkatenacja("abc", "de") == "abcde", "failed"
assert konkatenacja("asd", "fgh") == "asdfgh", "failed"
