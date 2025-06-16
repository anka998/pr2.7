sequence = input()
nums = list(map(int, sequence.split()))
positive_nums = [num for num in nums if num > 0]
print("Положительные числа:", positive_nums)
