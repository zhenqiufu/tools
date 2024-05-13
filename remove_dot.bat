@echo off
setlocal enabledelayedexpansion

set "inputFile=a.txt"
set "outputFile=b.txt"

if exist "%outputFile%" del "%outputFile%"

for /f "tokens=* delims=" %%a in (%inputFile%) do (
    set "line=%%a"
    set "tempLine="
    set "prevChar="
    for %%b in (!line!) do (
        if "%%b" NEQ "." (
            set "tempLine=!tempLine!%%b"
            set "prevChar=%%b"
        ) else (
            if "%%b" EQU "." if "!prevChar!" EQU "." (
                set "prevChar=%%b"
            ) else (
                set "tempLine=!tempLine!%%b"
                set "prevChar=%%b"
            )
        )
    )
    echo !tempLine!>>%outputFile%
)

echo "Processing complete."
