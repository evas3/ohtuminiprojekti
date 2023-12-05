*** Settings ***
Resource  resource.robot
Test Setup  Input Add Book Citation Command

*** Test Cases ***
Add Valid Book Citation
    Input Book Reference  Testikirja  Juho  2023  Otava  Osoite
    Output Should Contain  Book citation added succesfully!