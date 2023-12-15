*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

App Can Print Shortform Citations From File
    Input Create New BibTex File Command
    Input New BibTex Filename  Testitiedosto
    Input Add Book Citation Command
    Input Book Reference  Testikirja  Testaaja  2023  Otava  Osoite
    Input Summarize Written Citations Command
    Run Application
    Output Should Contain  | [Tes2023] | Book | Testaaja | 2023 |\n