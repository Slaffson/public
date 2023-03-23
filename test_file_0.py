money = float(input('Введите сумму вклада:  '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [rate * (money / 100) for rate in per_cent.values()]
deposit.sort(reverse = True)
print('Максимальная сумма, которую Вы сможете заработать: '
      + str(deposit[0]) + ' рублей!')

