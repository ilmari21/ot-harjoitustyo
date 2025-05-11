# Arkkitehtuuri

## Rakenne

Seuraava kaavio kuvaa sovelluksen luokka/pakkausrakennetta:

```mermaid
 classDiagram
    class ui {
        LoginView
        RegistrationView
        LogbookView
        AddFlightView
    }

    class services {
        LogbookService
    }

    class repositories {
        UserRepository
        LogbookRepository
    }

    class entities {
        User
        Flight
    }

    ui --> services
    services --> repositories
    services --> entities
    repositories --> entities
```

Kaaviossa **ui** vastaa käyttöliittymää ja sen eri näkymiä, **services** sisältää sovelluslogiikan, **repositories** tietokantaoperaatiot jaettuna *käyttäjä-* sekä *lokikirjatoimintoihin* ja **entities** sisältää objektit *User* ja *Flight*, jotka kuvaavat *käyttäjää* ja käyttäjän lentämää *lentoa*.

## Käyttöliittymä

Sovelluksessa on neljä sivua:

 - Kirjautumissivu (etusivu)
 - Rekisteröitymissivu
 - Lokikirjasivu (pääsivu)
 - Lentojen lisäyssivu

Kirjautumissivu on etusivu, josta voi siirtyä kirjautumalla lokikirjasivulle, tai jos haluaa luodan uuden käyttäjän, rekisteröitymissivulle. Lokikirjasivu on perusnäkymä, johon on listattu käyttäjän lisäämät lennot. Lokikirjasivulta voi siirtyä lentojen lisäysnäkymään, jossa käyttäjä voi lisätä uuden lennon. Näille jokaiselle on oma luokkansa.

## Sovelluslogiikka

Sovelluksen oleellisimmat luokat ovat [User](https://github.com/ilmari21/ot-harjoitustyo/blob/master/src/entities/user.py) ja [Flight](https://github.com/ilmari21/ot-harjoitustyo/blob/master/src/entities/flight.py). *User* kuvaa käyttäjää, ja *Flight* käyttäjän lentämää lentoa:

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
          elapsed_time
      }
```

Sovelluslogiikan toiminta toteutuu [LogbookService](https://github.com/ilmari21/ot-harjoitustyo/blob/master/src/services/logbook_service.py)-luokan kautta.

## Päätoiminnallisuudet

### Sisäänkirjautuminen

Tämä sekvenssikaavio kuvaa sisäänkirjautumista, ja sen alta löytyy tarkempi kuvaus tapahtumista:

```mermaid
sequenceDiagram
    participant User
    participant LoginView
    participant LogbookService
    participant UserRepository
    participant LogbookView

    User->>LoginView: Click "Login"
    activate LoginView
    LoginView->>LogbookService: login("teuvo", "testi")
    activate LogbookService
    LogbookService->>UserRepository: find_user("teuvo")
    activate UserRepository
    UserRepository-->>LogbookService: teuvo
    deactivate UserRepository
    LogbookService->>LogbookService: _user = teuvo
    LogbookService-->>LoginView: True
    deactivate LogbookService
    LoginView->>LogbookView: _logbook_view()
    deactivate LoginView
```

Kirjautumissivulla käyttäjä syöttää käyttäjätunnuksen ja salasanan, jonka jälkeen klikataan "Login"-painiketta. Tämä kutsuu `LogbookService`:n metodia `login`, joka kutsuu `UserRepository`:n metodia `find_user` löytääkseen käyttäjänimen ja sitä vastaavan salasanan. Jos käyttäjä löytyy, ja käyttäjänimi ja salasana täsmäävät, vaihtaa `LogbookService` tämän nykyiseksi käyttäjäksi, ja palauttaa tiedon onnistumisesta `LoginView`:lle. Tämä puolestaan vaihtaa näkymän lokikirjanäkymään.

### Uuden käyttäjän rekisteröiminen

Tämä sekvenssikaavio kuvaa käyttäjän rekisteröimistä, ja sen alta löytyy tarkempi kuvaus tapahtumista:

```mermaid
sequenceDiagram
    participant User
    participant RegistrationView
    participant LogbookService
    participant UserRepository
    participant teuvo
    participant LoginView

    User->>RegistrationView: Click "Register"
    activate RegistrationView
    RegistrationView->>LogbookService: validate_credentials("teuvo", "testi")
    activate LogbookService
    LogbookService-->>RegistrationView: (True, "")
    RegistrationView->>LogbookService: register_user("teuvo", "testi")
    LogbookService->>UserRepository: find_user("teuvo")
    activate UserRepository
    UserRepository-->>LogbookService: None
    deactivate UserRepository
    LogbookService->>User_Object: User(username, password)
    LogbookService->>UserRepository: create("teuvo")
    activate UserRepository
    UserRepository-->>LogbookService: teuvo
    deactivate UserRepository
    LogbookService-->>RegistrationView: teuvo
    deactivate LogbookService
    RegistrationView-->>User: Show success message
    RegistrationView->>LoginView: _login_view()
    deactivate RegistrationView
```

Rekisteröitymissivulla käyttäjä syöttää käyttäjätunnuksen sekä salaasanan ja klikkaa **"Register"**-painiketta. Tämä kutsuu `LogbookService`:n metodia `validate_credentials`, joka tarkistaa syötteet. Jos tarkistuksen menevät läpi, kutsutaan `LogbookService`:n metodia `register_user`. `LogbookService` kutsuu `UserRepository`:n metodia `find_user` jonka tarkoitus on varmistaa, ettei kyseinen käyttäjätunnus ole vielä käytössä. Jos käyttäjätunnus on vapaa, `UserRepository`:n metodi `create` luo uuden käyttäjän ja lisää sen tietokantaan. Tämän jälkeen tieto palautetaan `LogbookService`:lle ja siitä edelleen `RegistrationView`:lle, joka antaa käyttäjälle ilmoituksen siitä että uusi käyttäjä on luotu onnistuneesti ja siirtyy kirjautumissivulle.

### Lentojen lisääminen

Tämä sekvenssikaavio kuvaa lentojen lisäämistä, ja sen alta löytyy tarkempi kuvaus tapahtumista:

```mermaid
sequenceDiagram
    participant User
    participant LogbookView
    participant AddFlightView
    participant LogbookService
    participant LogbookRepository
    participant Flight

    User->>LogbookView: Click "Add flight"
    activate LogbookView
    LogbookView->>AddFlightView: _add_flight_view()
    deactivate LogbookView
    
    activate AddFlightView
    User->>AddFlightView: Enter aircraft_type, aircraft_reg, departure, arrival, dep_time, arr_time
    User->>AddFlightView: Click "Add flight"
    AddFlightView->>AddFlightView: _validate_entries()
    AddFlightView->>AddFlightView: _get_entries()
    AddFlightView->>LogbookService: create_flight_info(current_user, entries)
    activate LogbookService
    LogbookService->>LogbookService: _calculate_elapsed_time(dep_time, arr_time)
    LogbookService-->>AddFlightView: flight_info
    AddFlightView->>LogbookService: add_flight(flight_info)
    LogbookService->>Flight: Flight(flight_info)
    LogbookService->>LogbookRepository: create(flight)
    activate LogbookRepository
    LogbookRepository-->>LogbookService: flight
    deactivate LogbookRepository
    LogbookService-->>AddFlightView: flight
    deactivate LogbookService
    
    AddFlightView->>AddFlightView: _clear_entries()
    AddFlightView->>User: Show success message
    AddFlightView->>LogbookView: _logbook_view()
    deactivate AddFlightView
    
    activate LogbookView
    LogbookView->>LogbookView: _update_added_flights()
    deactivate LogbookView
```

Kun lokikirjasivulla painetaan **"Add flight"**-painiketta, kutsutaan metodia `show_add_flight` näkymän vaihtamiseksi jotta lento voidaan lisätä. Käyttäjä syöttää lentokoneen tyypin, rekisteritunnuksen, lähtö- ja saapumiskentän, sekä lähtö- ja saapumisajat, ja painaa **"Add flight"**-painiketta, joka tarkistettuaan syötteen kutsuu `LogbookService`:n metodia `create_flight_info`. Tämä metodi lisää annettujen syötteiden lisäksi lentäjän ja lentoajan, ja palauttaa lennon tiedot sanakirjana. Tämän jälkeen sanakirja annetaan `LogbookService`n metodille add_flight, joka puolestaan tarkistaa onko kirjauduttu sisään, eli onko käyttäjä olemassa, ja luo `Flight`-olion. Tämän jälkeen se kutsuu `LogbookRepository`:n `create`-metodia, joka tallettaa lennon tietokantaan. Tämä palauttaa tiedon `LogbookService`:lle ja siitä edelleen `AddFlightView`:lle, joka tyhjentää syötteet, antaa käyttäjälle ilmoituksen siitä että uusi lento on lisätty ja vaihtaa näkymän takaisin lokikirjanäkymään. `LogbookView` vielä päivittää listan käyttäjän lentämistä lennoista metodilla `update_added_flights`.

## Tietojen talletus

`LogbookService` käyttää repositorioita [LogbookRepository](https://github.com/ilmari21/ot-harjoitustyo/blob/master/src/repositories/logbook_repository.py) ja [UserRepository](https://github.com/ilmari21/ot-harjoitustyo/blob/master/src/repositories/user_repository.py), jotka tallettavat tiedot sovelluksen [data](https://github.com/ilmari21/ot-harjoitustyo/blob/master/data)-hakemistossa olevaan SQLite-tietokantaan. Tietokannan taulut ovat `flights` ja `users`. `LogbookRepository` vastaa lentojen tietokantaoperaatioista, `UserRepository` puolestaan käyttäjiin liittyvistä tietokantaoperaatioista. Testauksessa käytetään muistissa olevaa tietokantaa.

## Huomioitavaa

Sovelluksen syötteiden suuren määrän vuoksi oli valittava pitkien metodien ja useiden apumetodien välillä, joka joissakin kohdissa osoittautui ongelmalliseksi koodin siistinä pitämisen kannalta.
