def fun(a):
    otkr = a.count('(')
    zakr = a.count(')')
    if otkr > zakr:
        return 'Допишите', otkr - zakr, 'закрывающих скобок'
    elif otkr < zakr:
        return 'Допишите', zakr - otkr, 'открывающих скобок: '
    return 'Все скобки на месте'

print(fun(input('Введите строку: ')))
