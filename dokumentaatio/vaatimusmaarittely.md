# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen on tarkoitus mallintaa ilmailussa käytettävää **lokikirjaa**, johon *lentäjät* lisäävät tietoa lentämistään *lennoista*, kuten lähtö- ja kohdelentokenttä, konetyyppi ja rekisteritunnus, lähtö- ja saapumisaika.

## Käyttäjät

Sovelluksessa on vain yhdenlaisia käyttäjiä; *lentäjiä*.

## Sovelluksen toiminnallisuudet

### Kirjautumissivu (etusivu)

- Jos tunnus on olemassa käyttäjä voi kirjautua sisään, kunhan tunnus ja salasana täsmäävät
- Jos tunnusta ei ole, voi käyttäjä siirtyä rekisteröitymissivulle luomaan tunnuksen
 
### Rekisteröitymissivu

- Käyttäjä voi luoda käyttäjätunnuksen
  - Tunnukseen on lisättävä salasana, joka ei saa olla sama kuin käyttäjätunnus, ja tulee noudattaa minimi- ja maksimipituutta
  - Tunnuksen avulla voi kirjautua järjestelmään

### Lokikirjasivu (pääsivu)

- Kun käyttäjä on kirjautunut sisään, siirtyy hän pääsivulle, jossa hän voi
  - Lisätä uusia *lentoja*
  - Nähdä lisäämänsä lennot ja niiden tiedot; käyttäjä voi nähdä vain omat lentonsa

- Mahdollisuus nähdä tilastoja
  - Käyttäjäkohtaiset tilastot omista lennoista; lennettyjen lentojen määrä sekä kokonaislentotunnit

### Lentojen lisäämissivu

- Käyttäjä voi lisätä uuden lennon
  - Tarvittavat syötteet ovat lentokoneen tyyppi, lentokoneen rekisteritunnus, lähtö- ja saapumiskenttä, sekä lähtö- ja saapumisaika
