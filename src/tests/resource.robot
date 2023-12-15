*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Add New File For Test Citations
    Input  4
    Input  Testfile

Input Add Book Citation Command
    Input  1

Input Add Article Citation Command
    Input  2

Input Add Inproceedings Citation Command
    Input  3

Input Create New BibTex File Command
    Input  4

Input Summarize Written Citations Command
    Input  5

Input Search Reference Command
    Input  6

Input Delete Reference Command
    Input  7

Input Book Reference
    [Arguments]  ${title}  ${author}  ${year}  ${publisher}  ${address}
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${publisher}
    Input  ${address}

Input Article Reference
    [Arguments]  ${title}  ${author}  ${year}  ${journal}  ${volume}  ${pages}
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${journal}
    Input  ${volume}
    Input  ${pages}
    Run Application

Input Inproceedings Reference
    [Arguments]  ${title}  ${author}  ${year}  ${booktitle}
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${booktitle}
    Run Application

Input New BibTex Filename
    [Arguments]  ${filename}
    Input  ${filename}

Create New File And Fill With Data
    Input Create New BibTex File Command
    Input New BibTex Filename  Testitiedosto
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
