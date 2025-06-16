s = input()
nums = list(map(int, s.split()))
two_digit_positives = [num for num in nums if 10 <= num <= 99]
two_digit_positives.sort()
print("Положительные числа:", two_digit_positives)