### Käyttöohje

Projektin voi ladata [Releases](https://github.com/ilmari21/ot-harjoitustyo/releases)-osiosta klikkaamalla **Source code**.

## Sovelluksen käytön aloitus

1. Asenna poetry:

```
poetry install
```
tämä saattaa johtaa virheilmoitukseen "The current project could not be installed...", alustamisen pitäisi silti kuitenkin onnistua. Voit myös käyttää komentoa
```
poetry install --no-root
```
jolloin virheilmoitusta ei pitäisi tulla.

2. Alusta tietokanta:

```
poetry run invoke init-db
```

3. Sovelluksen käynnistäminen:

```
poetry run invoke start
```

## Kirjautumissivu

Kun sovelluksen käynnistää, siirtyy se kirjautumisnäkymään. Sisään voi kirjautua syöttämällä käyttäjätunnuksen ja salasanan, ja painamalla **"Login"**-painiketta.
Mikäli käyttäjätunnusta ei vielä ole, voi siirtyä uuden käyttäjän rekisteröimiseen painamalla **"New user"**-painiketta.
Mikäli kirjautuminen onnistuu, siirrytään ohjelman pääsivulle.

## Rekisteröitymissivu

Rekisteröitymissivulla voi luoda uuden käyttäjän, syöttämällä käyttäjätunnuksen sekä salasanan. Sekä käyttäjätunnuksen että salasanan tulee olla vähintään 5 merkkiä pitkät, tämän lisäksi käyttäjätunnuksen tulee olla vapaana.
Jos nämä ehdot täyttyvät, uusi käyttäjätunnus luodaan ja siirrytään kirjautumissivulle.

## Pääsivu

Pääsivulla perusnäkymässä on listattu käyttäjän lisäämät lennot, jos niitä on.
Mikäli haluaa lisätä uuden lennon, tulee painaa **"Add flight"**-painiketta. Tämän jälkeen näkymä vaihtuu, ja käyttäjän tulee syöttää lennon tiedot:

 - **Aircraft type**: lentokoneen tyyppi, pituuden tulee olla 4 merkkiä. Tarkoitus on käyttää [ICAO-tyyppitunnuksia](https://en.wikipedia.org/wiki/List_of_aircraft_type_designators)
 - **Aircraft registration**: lentokoneen tunnus, kuten OH-TKT
 - **Departure**: lähtökenttä, pituuden tulee olla 4 merkkiä. Tarkoitus on käyttää [ICAO-lentokenttätunnuksia](https://fi.wikipedia.org/wiki/Suomen_lentoasemat_ja_-paikat)
 - **Arrival**: saapumiskenttä, pituuden tulee olla 4 merkkiä. Tarkoitus on käyttää [ICAO-lentokenttätunnuksia](https://fi.wikipedia.org/wiki/Suomen_lentoasemat_ja_-paikat)
 - **Departure time**: lähtöaika, muodossa hh:mm
 - **Arrival time**: saapumisaika, muodossa hh:mm

Kun nämä syötteet on lisätty, painetaan **"Add flight"**-painiketta. Mikäli syötteet noudattavat ehtoja, ohjelma lisää lennon tietokantaan ja siirtyy takaisin perusnäykmään.
Lisäämäsi lento näkyy nyt myös listassa.

Painamalla **"Logout"**-painiketta voidaan kirjautua ulos, jolloin siirrytään takaisin kirjautumissivulle.
