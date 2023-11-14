*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command
import re

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallek  kalle123
    Output Should Contain  New user registered 

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle123  kalle123
    Output Should Contain  Username contains special characters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  k
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallek  kaaaaaaaaaaaaaaaaa
    Output Should Contain  Password too weak, no special characters
# ...

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command
