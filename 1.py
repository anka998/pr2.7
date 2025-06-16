str_s = input()
strings = str_s.split()
total_length = sum(len(s) for s in strings)
print("Сумма длин всех строк:", total_length)
