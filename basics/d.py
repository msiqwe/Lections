# def smallest():
#     numbers = set()
#     for _  in range(5):
#         num = int(input('Введи число: '))
#         numbers.add(num)
#     print('Smallest: ', min(num))
# smallest()

def credit():
    zaim = float(input('zaim: '))
    if zaim < 100000:
        print('Не менее 100000')
        return
    procent = 7.89
    total = zaim (zaim + (procent / 100))
    print('sum_w_procent: ', round(total, 2))

credit()

