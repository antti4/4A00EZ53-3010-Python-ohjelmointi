import calendar

k = int(input('Anna kuukauden numero (1-12): '))
v = int(input('Anna vuosi: '))
nimi = ''
p = 0
if k == 1:
    nimi = 'tammi'
    p = 31
elif k == 2:
    nimi = 'helmi'
    if calendar.isleap(v):
        p = 29
    else: 
        p = 28 
elif k == 3:
    nimi = 'maalis'
    p = 31
elif k == 4:
    nimi = 'huhti'
    p = 30
elif k == 5:
    nimi = 'touko'
    p = 31
elif k == 6:
    nimi = 'kesä'
    p = 30
elif k == 7:
    nimi = 'heinä'
    p = 31
elif k == 8:
    nimi = 'elo'
    p= 31
elif k == 9:
    imi = 'syys'
    p = 30
elif k == 10:
    nimi = 'loka'
    p = 31
elif k == 11:
    nimi = 'marras'
    p = 30
elif k == 12:
    nimi = 'joulu'
    p = 31
else:
    print('Kuukauden numero ei kelpaa!')
if p != 0:
    print(f'vuonna {v} {nimi}kuussa on {p} päivää')