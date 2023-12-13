*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

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

Add Invalid Year Book Citation Gives Error
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  ei vuosiluku  Otava  Osoite
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Year Article Citation Gives Error
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  Testaaja  ei vuosiluku  Tiede  14  132
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Year Inproceedings Citation Gives Error
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  Testaaja  ei vuosiluku  Testauksen alkeet
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Too Many Year Char Book Citation Gives Error
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  20223  Otava  Osoite
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Too Many Year Char Article Citation Gives Error
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  Testaaja  20223  Tiede  14  132
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Too Many Year Char Inproceedings Citation Gives Error
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  Testaaja  20223  Testauksen alkeet
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Author Book Citation Gives Error
    Input Add Book Citation Command
    Input Book Reference  Testikirja  1234  2023  Otava  Osoite
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Author Article Citation Gives Error
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  1234  2023  Tiede  14  132
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Author Inproceedings Citation Gives Error
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  1234  2023  Testauksen alkeet
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

App Can Print Shortform Citations From File
    Input Create New BibTex File Command
    Input New BibTex Filename  Testitiedosto
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
    Input Summarize Written Citations Command
    Run Application
    Output Should Contain  [Tes2023]Book: Testaaja, 2023\n
