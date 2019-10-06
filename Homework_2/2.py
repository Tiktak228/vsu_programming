a = input()
chisla = []
while a:
    chisla.append(a)
    a = input()
chisla = sorted(chisla, reverse=True)
print(''.join(chisla))
