numbers = [5, 2, 5, 2, 2, 20, 30, 200, 101, 320]

numbers2 = []
for number in numbers:
  if number not in numbers2:
    numbers2.append(number)
print(numbers2)