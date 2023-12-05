*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Add Book Citation Command
    Input  1

Input Book Reference
    [Arguments]  ${title}  ${author}  ${year}  ${publisher}  ${address}
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${publisher}
    Input  ${address}
    Run Application
