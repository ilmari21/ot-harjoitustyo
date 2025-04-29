# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen on tarkoitus mallintaa ilmailussa käytettävää **lokikirjaa**, johon *lentäjät* lisäävät tietoa lentämistään *lennoista*, kuten lähtö- ja kohdelentokenttä, konetyyppi ja rekisteritunnus, lähtö- ja saapumisaika.

## Käyttäjät

Sovelluksessa on vain yhdenlaisia käyttäjiä; *lentäjiä*. Mahdollista on myös lisätä uusi rooli, *kouluttaja*, joka voisi lisätä tietoa lentäjien lentämiin lentoihin, jos kyseessä on koulutuslento.

## Suunnitellut perusversion toiminnallisuudet

### Kirjautumissivu (etusivu)

- Jos tunnus on olemassa käyttäjä voi kirjautua sisään, kunhan tunnus ja salasana täsmäävät **"tehty"**
- Jos tunnusta ei ole, voi käyttäjä siirtyä rekisteröitymissivulle luomaan tunnuksen **"tehty"**
 
### Rekisteröitymissivu

- Käyttäjä voi luoda käyttäjätunnuksen
  - Tunnukseen on lisättävä salasana, joka ei saa olla sama kuin käyttäjätunnus, ja tulee noudattaa minimi- ja maksimipituutta **"tehty"**
  - Tunnuksen avulla voi kirjautua järjestelmään **"tehty"**

### Pääsivu

- Kun käyttäjä on kirjautunut sisään, siirtyy hän pääsivulle, jossa hän voi
  - Lisätä uusia lentoja **"tehty"**
  - Nähdä lisäämänsä lennot ja niiden tiedot; käyttäjä voi nähdä vain omat lentonsa **"tehty"**

## Mahdolliset laajemmat toiminnallisuudet

- Mahdollisuus nähdä tilastoja
  - Käyttäjäkohtaiset tilastot omista lennoista, kuten kokonaislentotunnit **"tehty osittain: lisättyjen lentojen määrä näkyy pääsivulla"**
  - Tilastoja eri lentopaikoista, kuten lentojen ja kävijöiden määrä
  - Tilastoja lentokoneista, kuten lentotunnit, lentojen ja eri lentäjien määrä
 
- Hakuominaisuus, omalla sivullaan
  - Haku lentopaikan, konetyypin tai tietyn koneen perusteella
 
- Profiilisivut, johon vain käyttäjä pääsee
  - Mahdollisuus lisätä ja muokata omia tietojaan
 
- Mahdollisuus lisätä tarkempia tietoja lennoista, kuten
  - Laskeutumisten määrä
  - Lennon tyyppi, esim. koulutuslento
