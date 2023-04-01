tickets = int(input('Сколько билетов Вы хотите купить: '))
age = list(map(int, input('Введите возраст лиц через пробел: ').split()))
if tickets != len(age):
    print('Вы не указали возраст каждого из регистрируемых лиц! дальнейший расчет суммы невозможен,\n')
    print('-----------------------------------------------------------------------------')
    raise ValueError
L = 0 # количество билетов за 0 рублей
M = 0 # количество билетов за 990 рублей
H = 0 # количество билетов за 1390 рублей
for a in age:
    if a in range(1, 18):
        L = L + 1
    elif a in range(18, 26):
        M = M + 1
    elif a >= 26:
        H = H + 1
Prices = [0, 990, 1390]
price_total = L * Prices[0] + M * Prices[1] + H * Prices[2]
if tickets >= 3:
    price_total = price_total * 0.9
print(f'Итого к оплате {price_total} рублей')
