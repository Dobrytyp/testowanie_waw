# Szukanie błędów

# import math
# def circle_areas(r):
#     if type(r) not in [int, float]:
#         return "Wpisz prawdisłową wartość"
#     elif r<0:
#         return "Kolo o takim promieniu nie istnieje"
#     else:
#         return math.pi*r**2
#
#
# print(circle_areas(6))
# print(circle_areas(-4))
# print(circle_areas("asd"))
# print(circle_areas(2+5j))
# print(circle_areas(-4))

### ALE Można łapać wyjątki (try i except)

# import math
# def circle_areas(r):
#     try:
#         return math.pi*r**2
#     except:
#         return "coś poszło nie tak"
#
# print(circle_areas(6))
# print(circle_areas(-4))
# print(circle_areas("asd"))
# print(circle_areas(2 + 5j))
# print(circle_areas(-4))

# Komenda raise rzuca wyjątek, Może ospisywać błędy, dzięki czemu będą bardziej zrozumiały.

import math
def circle_areas(r):
    if r < 0:
        raise Exception("promień nie może być ujemny")
    try:
        return math.pi*r**2
    except:
        return "coś poszło nie tak"

print(circle_areas(6))
print(circle_areas(-4))
print(circle_areas("asd"))
print(circle_areas(2 + 5j))
print(circle_areas(-4))