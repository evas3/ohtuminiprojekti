*** Settings ***
Resource  resource.robot
Test Setup  Input Add New File For Test Citations

Add Valid Article Citation
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  Testaaja  2023  Tiede  14  132
    Output Should Contain  \nArticle citation added succesfully!\n

Add Valid Inproceedings Citation
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  Testaaja  2023  Testauksen alkeet
    Output Should Contain  \nInproceedings citation added succesfully!\n

Add Invalid Year Article Citation Gives Error
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  Testaaja  ei vuosiluku  Tiede  14  132
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Year Inproceedings Citation Gives Error
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  Testaaja  ei vuosiluku  Testauksen alkeet
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Too Many Year Char Article Citation Gives Error
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  Testaaja  20223  Tiede  14  132
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Too Many Year Char Inproceedings Citation Gives Error
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  Testaaja  20223  Testauksen alkeet
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Author Article Citation Gives Error
    Input Add Article Citation Command
    Input Article Reference  Testiartikkeli  1234  2023  Tiede  14  132
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n

Add Invalid Author Inproceedings Citation Gives Error
    Input Add Inproceedings Citation Command
    Input Inproceedings Reference  Testi  1234  2023  Testauksen alkeet
    Run Application
    Output Should Contain  \nauthor must be letters and year max 4 numbers, continue:\n