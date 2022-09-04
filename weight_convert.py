# 1 >>> 2.20462

weight = int(input('please put your weight: '))

forma = input(('(L) bs  or (K) g:  ')).lower()

if forma == 'l':
  new_weight = weight * 0.45
  print(f'You are {round(new_weight, 2)}  kg')
elif forma == 'k':
  new_weight = weight / 0.45
  print(f'You ar {round(new_weight, 2) } lbs')
else:
  print(int(input('please put your right weight: ')))