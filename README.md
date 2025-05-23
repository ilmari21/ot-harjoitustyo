# Ohjelmistotekniikka, harjoitustyö

Sovellus mallintaa **virtuaalista lokikirjaa**, johon *käyttäjä* voi lisätä lentämänsä *lennot*.

Sovellukseen voi kirjautua luotuaan käyttäjätunnuksen, jonka jälkeen voi lisätä lentoja syöttämällä lentokoneen tyypin, tunnuksen sekä lähtö- ja saapumiskentät. Tässä kohtaa sovellus ei tarkista lentokoneen tyypistä ja lentokentistä muuta kuin sen, että merkkejä on 4, mutta tarkoitus on noudattaa ICAO-standardeja. Suomen lentokenttien ICAO-koodeja löytää kuitenkin mm. [täältä](https://fi.wikipedia.org/wiki/Suomen_lentoasemat_ja_-paikat), ja lentokoneiden ICAO-tyyppitunnuksia [täältä](https://en.wikipedia.org/wiki/List_of_aircraft_type_designators). Lisäksi on syötettävä lähtö- ja saapumisaika, muodossa hh:mm.

## Python-versio

Testattu Pythonin versiolla **`3.10`**.

## Linkit

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Releaset

- [Viikko 5](https://github.com/ilmari21/ot-harjoitustyo/releases/tag/viikko5)
- [Viikko 6](https://github.com/ilmari21/ot-harjoitustyo/releases/tag/viikko6)
- [Loppupalautus](https://github.com/ilmari21/ot-harjoitustyo/releases/tag/loppupalautus)

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

## Sovelluksen testaaminen

Staattisen analyysin koodista voi luoda komennolla:

```
poetry run invoke lint
```

Sovellusta voi testata suorittamalla komento:

```
poetry run invoke test
```

ja kattavuusraportin voi luoda komennolla:

```
poetry run coverage-report
```
