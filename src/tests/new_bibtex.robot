*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

Create A New BibTex File
    Input Create New BibTex File Command
    Input New BibTex Filename  Testitiedosto
    Run Application
    Output Should Contain  \nNew file with a name Testitiedosto created\n