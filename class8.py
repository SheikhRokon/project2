# def product(*args):
#     sum = 0
#     for result in args:
#         sum += result

#     return sum

# belal = product(35,25,58,85)
# print("Total price :",belal)

# juba = product(35,85)
# print("Total price :",juba)

# ruba = product(35,85)
# print("Total price :",ruba)


def product(*args):
    # print(type(args))
    sum = 0
    for result in args:
        sum += result

    return sum

belal = product(35,25,58,85)
print("Total price :",belal)

juba = product(35,85)
print("Total price :",juba)

ruba = product(35,85)
print("Total price :",ruba)




