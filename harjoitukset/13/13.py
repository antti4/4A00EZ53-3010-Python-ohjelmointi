def on_palindromi(sana):
    characters = "!@#$%^&*()-_=+[{]}|;:'\",<.>/? \\"
    for char in characters:
        sana = sana.replace(char, "")
    takaperin = ''.join(list(reversed(sana)))
    return sana.lower() == takaperin.lower()

ehdokkaat = [
'A man, a plan, a canal: Panama.',
'Iso rikas sika sökösakissa kirosi.',
'"Aa, viinaa sitruksilla", kallis kurtisaani ivaa.',
'Joku satunnainen lause'
]
for e in ehdokkaat:
    tulos = 'EI OLE'
    if on_palindromi(e):
        tulos = 'ON'
    print(f'"{e}": {tulos} palindromi')