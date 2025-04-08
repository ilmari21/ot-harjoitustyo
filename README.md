# Ohjelmistotekniikka, harjoitustyö

Tavoitteeni on luoda **virtuaalinen lokikirja**, johon *käyttäjä* voi lisätä lentämänsä *lennot*.

## Linkit

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Sovelluksen käytön aloitus

1. Asenna poetry

```
poetry install
```

2. Alusta tietokanta

```
poetry run invoke init-db
```

3. Sovelluksen käynnistäminen

```
poetry run invoke start
```

## Sovelluksen testaaminen

Staattisen analyysin koodista voi luoda komennolla

```
poetry run invoke lint
```

Sovellusta voi testata suorittamalla komento

```
poetry run invoke test
```

ja kattavuusraportin voi luoda komennolla

```
poetry run coverage-report
```
