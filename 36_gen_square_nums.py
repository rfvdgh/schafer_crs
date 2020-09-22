# def square_numbers(nums):
#     # result = []
#     # for i in nums:
#     #     result.append(i * i)
#     # return result

#     # generator solution
#     for i in nums:
#         yield (i * i)


# my_nums = square_numbers([1, 2, 3, 4, 5])
my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(my_nums)
# print(list(my_nums))
# print(next(my_nums)) # you will get stopiteration exception if you run this code several more times

for num in my_nums:
    print(num)
