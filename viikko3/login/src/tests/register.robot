*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle2
    Set Password  kalle1234
    Set Password confirmation  kalle1234
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Letters And Numbers
    Set Username  kalle2
    Set Password  kalle123
    Set Password confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Letters And Special Characters
    Set Username  kalle2
    Set Password  kalle#abc
    Set Password confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password And Confirmation
    Set Username  kalle2
    Set Password  kalle123
    Set Password confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Different Password And Confirmation
    Set Username  kalle2
    Set Password  kalle123
    Set Password confirmation  kalle456
    Click  button >> text=Register
    Register Should Fail With Message  Password confirmation does not match

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle1234
    Set Password confirmation  kalle1234
    Click  button >> text=Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  1234567
    Set Password confirmation  1234567
    Click  button >> text=Register
    Register Should Fail With Message  Password should be at least eight digits

Register Rejects Password Containing Only Lowercase Letters
    Set Username  kalle2
    Set Password  kallekalle
    Set Password confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Error

Register Rejects Password Containing Only Uppercase And Lowercase Letters
    Set Username  kalle2
    Set Password  KalleKalle
    Set Password confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Error

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  12345678
    Set Password confirmation  12345678
    Click  button >> text=Register
    Register Should Fail With Message  Said username already in use

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Register Should Fail With Error
    Register Page Should Be Open
    ${message}=  Get Text  css=ul li
    Should Not Be Empty  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Starting Page
    Click  text=Register new user
    Set Username  kalle
    Set Password  kalle123
    Set Password confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed
    Go To Register Page

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation