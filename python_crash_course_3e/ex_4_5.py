list_of_nums = [*range(1,11)]
max_num = max(list_of_nums)
min_num = min(list_of_nums)
print(f"Max number is {max_num}")
print(f"Min number is {min_num}")

sum = 0
for num in list_of_nums:
    sum += num

print(f"Sum is {sum}")
