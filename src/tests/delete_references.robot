*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

*** Test Cases ***
Delete Reference Valid
    Input Delete Reference Command
    Input  Tes2023  
    Input  y
    Run Application
    Output Should Contain  \nReference deleted\n

Delete Reference Incorrect
    Input Delete Reference Command
    Input  Tei2023  
    Input  y
    Run Application
    Output Should Contain  \nFailed to delete\n
