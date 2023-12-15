*** Settings ***
Resource  resource.robot

*** Test Cases ***
User Can Search For Author And Author Is Found
    Create New File And Fill With Data
    Input Search Reference Command
    Input  author
    Input  Testaaja
    Run Application
    Output Should Contain  @book{Tes2023,

User Can Search For Author And Author Is Not Found
    Create New File And Fill With Data
    Input Search Reference Command
    Input  author
    Input  testaaja1
    Run Application
    Output Should Contain  No references found\n