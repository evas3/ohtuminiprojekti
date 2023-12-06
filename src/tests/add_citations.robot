*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Valid Book Citation
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
    Output Should Contain  \nBook citation added succesfully!\n

Add Valid Article Citation
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  Testaaja  2023  Tiede  14  132
    Output Should Contain  \nArticle citation added succesfully!\n

Add Valid Inproceedings Citation
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  Testaaja  2023  Testauksen alkeet
    Output Should Contain  \nInproceedings citation added succesfully!\n

Create A New BibTex File
    Input Create New BibTex File Command
    Input New BibTex Filename  Testitiedosto
    Output Should Contain  \nNew file with a name Testitiedosto created\n