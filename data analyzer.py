Sm = 0
i = 0
nameold = 0
woman = 0
for c in range(1,5):
    print(f'----- {c}ª PEOPLE -----')
    name = str(input('Name:  '))
    old = int(input('Years old: '))
    Sexo = str(input('Male or Female [M/F]: ')).upper()
    Sm += old
    if old > i :
        i = old
        nameold = name
    if Sexo == 'F'   and old < 20 :
        woman += 1
Oa = Sm / 4
print(f'The average age of the group is {Oa} years old ')
print(f'The oldest man in group has {i} years old and his name is {nameold}.')
print(f'The group have {woman} womans with less 20 years old')
c=str(input('finish'))