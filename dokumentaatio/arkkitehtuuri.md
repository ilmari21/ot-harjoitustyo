# Arkkitehtuuri

## Käyttöliittymä

Sovelluksessa on kolme sivua:

 - Kirjautumissivu
 - Rekisteröitymissivu
 - Pääsivu

Kirjautumissivu on etusivu, josta voi siirtyä kirjautumalla pääsivulle, tai jos haluaa luodan uuden käyttäjän, rekisteröitymissivulle. Pääsivulla voi lisätä uusia lentoja.

## Sovelluksen logiikka

Sovelluksen oleellisimmat luokat ovat *User* ja *Flight*. *User* kuvaa käyttäjää, ja *Flight* käyttäjän lentämää lentoa:

```mermaid
 classDiagram
      Flight "*" --> "1" User
      class User{
          username
          password
      }
      class Flight{
          pilot
          aircraft_type
          aircraft_reg
          departure
          arrival
          dep_time
          arr_time
      }
```

## Päätoiminnallisuudet

### Lentojen lisääminen

Tämä sekvenssikaavio kuvaa lentojen lisäämistä, ja sen alta löytyy tarkempi selitys tapahtumista:

```mermaid
 sequenceDiagram
    participant User
    participant MainView
    participant LogbookService
    participant LogbookRepository
    participant flight

    User->>MainView: Click "Add flight"
    activate MainView
    MainView->>MainView: show_add_flight()
    
    User->>MainView: Enter aircraft_type, aircraft_reg, departure, arrival, dep_time, arr_time
    User->>MainView: Click "Add flight"
    MainView->>LogbookService: add_flight(aircraft_type, aircraft_reg, departure, arrival, dep_time, arr_time)
    activate LogbookService
    LogbookService->>flight: Flight(pilot, aircraft_type, aircraft_reg, departure, arrival, dep_time, arr_time)
    LogbookService->>LogbookRepository: create(flight)
    activate LogbookRepository
    LogbookRepository-->>LogbookService: flight
    deactivate LogbookRepository
    LogbookService-->>MainView: flight
    deactivate LogbookService

    MainView->>MainView: show_main_view()
    MainView->>MainView: update_added_flights_list()
    deactivate MainView
```

Kun pääsivulla painetaan **"Add flight"**-painiketta, kutsutaan MainViewin metodia `show_add_flight` näkymän vaihtamiseksi jotta lento voidaan lisätä. Käyttäjä syöttää lähtö- ja saapumiskentän, sekä lähtö- ja saapumisajat, ja painaa **"Add flight"**-painiketta, joka tarkistettuaan syötteen kutsuu `LogbookService`:n metodia `add_flight`. Tämä puolestaan tarkistaa onko kirjauduttu sisään, eli onko käyttäjä olemassa, ja luo `Flight`-olion käyttämällä aikaisempia syötteitä ja lisäämällä siihen lentäjän, käyttämällä `LogbookRepository`:n `create`-metodia. Tämä palauttaa tiedon LogbookService:lle ja siitä edelleen MainView:lle, joka vaihtaa näkymän takaisin normaaliksi metodilla `show_main_view`, joka vielä päivittää listan käyttäjän lentämistä lennoista metodilla `update_added_flights_list`.
