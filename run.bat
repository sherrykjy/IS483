@echo off

REM Set the root directory of your Git repository
set ROOT_DIR=%CD%

REM Loop through files in the specified folder
for %%f in ("%ROOT_DIR%\utils\*.py") do (
    REM Check if the file name does not end with "_test.py"
    echo %%~nf | find /i "_test" > nul
    if errorlevel 1 (
        REM Execute the Python file
        start cmd /k "python %%f"
    )
)

REM Install dependencies and run the UI
cd h365
start cmd /k "npm install && npm run serve"
