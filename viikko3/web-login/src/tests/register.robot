*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go Register

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Confirm  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Confirm  kalle123
    Submit Credentials
    Register Should Fail

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalleaaaaaaa
    Set Confirm  kalleaaaaaaa
    Submit Credentials
    Register Should Fail
# # salasana ei sisällä halutunlaisia merkkejä
# # ...

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Confirm  kalle122
    Submit Credentials 
    Register Should Fail
# # ...

Login After Successful Registration
    Set Username  kallek
    Set Password  kalle123
    Set Confirm  kalle122
    Submit Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Click Button  Login
    Set Username  kallek
    Set Password  kalle123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  k
    Set Password  kalle123
    Set Confirm  kalle122
    Submit Credentials

    Click Link  Login
    Set Username  k
    Set Password  kalle123
    Click Button  Login
    Login Should Fail

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open
Login Should Fail
    Login Page Should Be Open


Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail
    Register Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirm
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Go Register
    Go To Register Page
    Register Page Should Be Open