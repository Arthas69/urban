first = int(input())
second = int(input())
third = int(input())

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)


# Or second variant

# nums = {first, second, third}
#
# if len(nums) == 1:
#     print(3)
# elif len(nums) == 2:
#     print(2)
# else:
#     print(0)

