# Työn documentointi
### Käynnistys
komentotulkissa
>python main.py
### Walkthrough
kometotulkin vähimmäiskäskyt:
>ota luu<br />
>mene pohjoiseen<br />
>mene länteen<br />
>mene länteen<br />
>lyö luu<br />
>mene etelään<br />
>ota kivihakku<br />
>mene pohjoiseen<br />
>mene länteen<br />
>lyö hakku<br />
>mene länteen<br />
>mene länteen<br />
>ota kivipatsas<br />
>mene pohjoiseen<br />
>käytä kivipatsas<br />
>mene pohjoiseen<br />
>ota avain1<br />
>mene etelään<br />
>mene etelään<br />
>mene länteen<br />
>ota avain2<br />
>yhdistä avain1 avain2<br />
>mene itään<br />
>mene itään<br />
>mene itään<br />
>mene itään<br />
>mene itään<br />
>mene itään<br />
>käytä avain<br />
>mene pohjoiseen<br />
## Koodista
json on ainoa importattu työkalu, muuten kaikki käytettävät ominaisuukset ovat pythonin sisäisiä, kuten if ja for lauseet, stringin ominaisuukset värien kanssa ja kaikki muu ohjelmakielen peruskyvyt.
Koodin tietorakenteet seuraa jsonin käytäntöjä ja lähettää json tiedostosta haetun pelaajadatan ja kenttädatan taulukkona nimeltä gameItems muun koodin käytettäväksi. Tein koodin tässä muodossa, jotta peliin voisi helposti lisätä "kenttiä" enemmän kuin yhden ja vain vaihtaa, mitä json tiedostoa lukea. Pelaamisen aikana gameItemsin dataan tehdään muutoksia, mutta "tallentamista" ei ole toteutettu pelille, joten kaikki edistys katoaa pelin lopettamisen jälkeen.
## Pelistä
Pelissä pelaaja herää vankilasta ja hänen täytyy hakea vankilan itä-siivestä kaksi avaimen puolikasta, yhdistää ne ja palata tyrmänsä edessä olevaan oven luokse ja avata se saamallansa avaimella. Pelissä pelaajan ja avainten väliin tulee useita esteitä, kuten hirviö, sortunut katto ja kivisiä ovia, jotka pakottavat pelaajaa käyttämään maasta löytäneitä esineitä lyömällä, hyödyntämällä tai yhdistämällä niitä. Pelissä on myös ei-pakollinen paikka jonka päästä löytyy tyhjä avaamisen tarpeessa oleva aarrearkku. Pelin voittaa jos astuu ulos avatusta ovesta vapauteen.
