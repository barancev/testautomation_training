*** Settings ***
Library       OperatingSystem

*** Test Cases ***
Test File Creation
    [Template]    Can Create File With Name ${name}
    test.txt
    .txt
    @#$%^&

*** Keywords ***
Can Create File With Name ${file_name}
    Create Directory    ${TEMPDIR}/tmp
    Create File         ${TEMPDIR}/tmp/${file_name}
    File Should Exist   ${TEMPDIR}/tmp/${file_name}
    Remove Directory    ${TEMPDIR}/tmp/     True
