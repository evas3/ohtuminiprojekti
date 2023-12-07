# OHTU miniprojekti

![GHA workflow badge](https://github.com/evas3/ohtuminiprojekti/workflows/CI/badge.svg) 
[![codecov](https://codecov.io/gh/evas3/ohtuminiprojekti/graph/badge.svg?token=LBHUEB6DP0)](https://codecov.io/gh/evas3/ohtuminiprojekti)

## Dokumentaatio
Projektin [product backlog ja sprinttien 1-3 backlogit](https://docs.google.com/spreadsheets/d/1Exh5aVcuuAFeJxPsNNVsdo74kYu4kWRfEj65Jobz8Fs/)


## Definition of Done
Valmiksi saatu toiminnallisuus on suunniteltu etukäteen ja toteutettu. Lisäksi sen toiminta on varmistettu testaamalla ja toiminnallisuus on integroitu osaksi muuta ohjelmistoa tuotantoympäristössä.

## Asennusohje
Projektin riippuvuudet asennetaan seuraavalla komennolla
```
poetry install
```

## Käyttöohje
Ohjelmann suorittaminen onnistuu komennolla
```
poetry run invoke start
```
Tämän jälkeen käyttäjän tulee seurata ohjelman antamia ohjeita.

Kun käyttäjä on valinnut viitetyypin ja antanut vaaditut kentät, BibTex muotoinen viite löytyy tiedostosta src/data/references.bib. Kun viitetyyppi on valittu, BibTex muotoisen tiedoston sisällön näkee halutessa komennolla
```
poetry run invoke list
```
