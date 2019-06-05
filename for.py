def total(x, y):
    count = x
    for i in range(1, 10):
        count += i
    return count


print(total(3, 5))

# def total(initial=5, *numbers):
# #     for number in numbers:
# #         count += number
# #     for key in keywords:
# #         count += keywords[key]