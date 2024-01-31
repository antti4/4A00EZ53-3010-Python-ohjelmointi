#energia
perus = 1.98 #euro/kk
maksu = 7.09 #sentti/kWh
#siirto
siirtoperus = 4.77 # euro/kk
siirtomaksu = 2.9264 #sentti/kWh
vero = 2.79372 #sentti/kWh
#kuut
lokakuu = 642.934#kWh
marraskuu = 674.345 #kWh
joulukuu = 757.599#kWh

#hinnat
lokahinta = perus+(maksu*lokakuu/100.0)+ siirtoperus+(siirtomaksu*lokakuu/100.0)+(vero*lokakuu/100.0)
marrashinta = perus+(maksu*marraskuu/100.0)+ siirtoperus+(siirtomaksu*marraskuu/100.0)+(vero*marraskuu/100.0)
jouluhinta = perus+(maksu*joulukuu/100.0)+ siirtoperus+(siirtomaksu*joulukuu/100.0)+(vero*joulukuu/100.0)
print(lokahinta+marrashinta+jouluhinta)