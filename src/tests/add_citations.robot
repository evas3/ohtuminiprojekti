*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Valid Book Citation
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
    Run Application
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
    Run Application
    Output Should Contain  \nNew file with a name Testitiedosto created\n

Add Invalid Book Citation Gives Error
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  ei vuosiluku  Otava  Osoite
    Run Application
    Output Should Contain  \nCould not validate the inputs, use alphabets and numbers correctly!\n

Add Invalid Article Citation Gives Error
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  Testaaja  ei vuosiluku  Tiede  14  132
    Output Should Contain  \nCould not validate the inputs, use alphabets and numbers correctly!\n

Add Invalid Inproceedings Citation Gives Error
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  Testaaja  ei vuosiluku  Testauksen alkeet
    Output Should Contain  \nCould not validate the inputs, use alphabets and numbers correctly!\n

App Can Print Shortform Citations From File
    Input Create New BibTex File Command
    Input New BibTex Filename  Testitiedosto
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
    Input Summarize Written Citations Command
    Run Application
    Output Should Contain  [Tes2023]Book: Testaaja, 2023\n
