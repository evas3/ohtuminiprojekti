*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

*** Test Cases ***
Delete Reference
    Input Delete Reference Command
    Input  Tes2023  
    Input  y
    Run Application
    Output Should Contain  \nReference deleted\n
