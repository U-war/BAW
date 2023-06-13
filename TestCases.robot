*** Settings ***
Documentation    This test suite is created for perform automated tests on WebGoat application.
...              Authors:
...              Arkadiusz Kotynia
...              Urszula Warminska
Library    resources.py
Library    OperatingSystem
Library    String

Suite Setup    Suite Setup
Test Setup    Test Setup
*** Test Cases ***
SQL injection (intro) 2
    What is SQL?

SQL injection (intro) 3
    Data Manipulation Language(DML)

SQL injection (intro) 4
    Data Definition Language (DDL)

SQL injection (intro) 5
    Data Control Language (DCL)

Crypto Basics 2
    Base64 Encoding

Crypto Basics 6
    RSA Private Key

Secure Passwords 4
    How long could it take to brute force your password?

*** Keywords ***
Suite Setup
    register_user  test-user  Pass123


Test Setup
    ${driver}=  login  test-user  Pass123
    Set Test Variable    ${DRIVER}  ${driver}

What is SQL?
    ${DRIVER}=  switch_to_injection  ${DRIVER}
    ${outcome}=  what_is_sql  ${DRIVER}
    Should Contain    ${outcome}  succeeded
    [Teardown]    close_window  ${DRIVER}

Data Manipulation Language(DML)
    ${DRIVER}=  switch_to_injection  ${DRIVER}
    ${outcome}=  data_manipulation_language  ${DRIVER}
    Should Contain    ${outcome}  Congratulations
    [Teardown]    close_window  ${DRIVER}

Data Definition Language (DDL)
    ${DRIVER}=  switch_to_injection  ${DRIVER}
    ${outcome}=  data_definition_language  ${DRIVER}
    Should Contain    ${outcome}  Congratulations
    [Teardown]    close_window  ${DRIVER}

Data Control Language (DCL)
    ${DRIVER}=  switch_to_injection  ${DRIVER}
    ${outcome}=  data_control_language  ${DRIVER}
    Should Contain    ${outcome}  Congratulations
    [Teardown]    close_window  ${DRIVER}

RSA Private Key
    ${DRIVER}=  switch_to_cryptographic_failures  ${DRIVER}
    ${key}=  private_key  ${DRIVER}
    Log  ${key}  console=true
    RUN  echo "${key}" > test.key
    RUN  openssl rsa -in test.key -pubout > test.pub
    ${out}=  RUN  openssl rsa -in test.pub -pubin -modulus -noout
    @{mod}=  Split String  ${out}  =
    Log  ${mod}  console=true
    ${base}=  RUN  echo -n "${mod}[1]" | openssl dgst -sign test.key -sha256 | base64
    Log    ${base}  console=true
    ${outcome}=  paste_response  ${DRIVER}  ${mod}[1]  ${base}
    Should Contain  ${outcome}  Congratulations
    [Teardown]    close_window  ${DRIVER}

Base64 Encoding
    ${DRIVER}=  switch_to_cryptographic_failures  ${DRIVER}
    ${base_encoded}=  encoding_base64  ${DRIVER}
    @{split}=  Split String    ${base_encoded}
    ${output}=  RUN  echo "${split}[2]" | base64 --decode
    @{result}=  Split String    ${output}  :
    ${outcome}=  paste_decoded  ${DRIVER}  ${result}[0]  ${result}[1]
    Should Contain  ${outcome}  Congratulations
    [Teardown]    close_window  ${DRIVER}

How long could it take to brute force your password?
    ${DRIVER}=  switch_to_identity_auth_failure  ${DRIVER}
    ${outcome}=  how_long  ${DRIVER}
    Should Contain  ${outcome}  succeeded
    [Teardown]    close_window  ${DRIVER}

