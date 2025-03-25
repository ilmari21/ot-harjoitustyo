# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen on tarkoitus mallintaa ilmailussa käytettävää **lokikirjaa**, johon *lentäjät* lisäävät tietoa lentämistään *lennoista*, kuten lähtö- ja kohdelentokenttä, laskeutumisten määrä, konetyyppi ja rekisteritunnus, lähtö- ja saapumisaika, ja lennon tyyppi (esim. koulutuslento).

## Käyttäjät

Sovelluksessa on vain yhdenlaisia käyttäjiä; *lentäjiä*. Mahdollisuus on myös lisätä uusi rooli, *kouluttaja*, joka voisi lisätä tietoa lentäjien lentämiin lentoihin, jos kyseessä on koulutuslento.

## Suunnitellut perusversion toiminnallisuudet

### Kirjautumissivu

- Käyttäjä voi luoda käyttäjätunnuksen
  - Tunnukseen on lisättävä salasana, joka ei saa olla sama kuin käyttäjätunnus, ja tulee noudattaa minimi- ja maksimipituutta
  - Tunnuksen avulla voi kirjautua järjestelmään
  - Luotuaan tunnuksen käyttäjä voi kirjautua sisään, kunhan tunnus ja salasana täsmäävät

### Pääsivu

- Kun tunnus on olemassa, ja käyttäjä on kirjautunut sisään, hän voi:
  - Lisätä uusia lentoja
  - Nähdä lisäämänsä lennot ja niiden tiedot; käyttäjä voi nähdä vain omat lentonsa

## Mahdolliset laajemmat toiminnallisuudet

- Mahdollisuus nähdä tilastoja
  - Käyttäjäkohtaiset tilastot omista lennoista, kuten kokonaislentotunnit
  - Tilastoja eri lentopaikoista, konetyypeistä ja yksittäisistä koneista
 
- Hakuominaisuus, omalla sivullaan
  - Haku lentopaikan, konetyypin tai tietyn koneen perusteella
