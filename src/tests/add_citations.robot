*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

*** Test Cases ***
Add Valid Book Citation
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
    Run Application
    Output Should Contain  \nBook citation added succesfully!\n

Add Invalid Year Book Citation Gives Error
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  ei vuosiluku  Otava  Osoite
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Too Many Year Char Book Citation Gives Error
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  20223  Otava  Osoite
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Author Book Citation Gives Error
    Input Add Book Citation Command
    Input Book Reference  Testikirja  1234  2023  Otava  Osoite
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n
