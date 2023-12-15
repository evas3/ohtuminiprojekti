*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

*** Test Cases ***
Delete Reference
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
    Run Application
    Output Should Contain  \nBook citation added succesfully!\n
