*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

*** Test Cases ***
App Can Print Shortform Citations From File
    Create New File And Fill With Data
    Input Summarize Written Citations Command
    Run Application
    Output Should Contain  | [Tes2023] | Book | Testaaja | 2023 |\n