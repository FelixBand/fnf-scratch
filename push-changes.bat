rd /s /q "Friday Night Funkin'"

ren "Friday Night Funkin'.sb3" "Friday Night Funkin'.zip"

powershell -NoProfile -Command ^
    "& {Expand-Archive -Path 'Friday Night Funkin''s 2.zip' -DestinationPath 'Friday Night Funkin''s 2'}"

ren "Friday Night Funkin'.zip" "Friday Night Funkin'.sb3"

git add .

REM Commit changes with a timestamp. Ignore the jank, I hate Windows
for /f "tokens=2 delims==" %%a in ('"wmic OS Get localdatetime /value"') do set datetime=%%a
set year=%datetime:~0,4%
set month=%datetime:~4,2%
set day=%datetime:~6,2%
set hour=%datetime:~8,2%
set minute=%datetime:~10,2%
set second=%datetime:~12,2%

set commit_msg=Updated project - %year%-%month%-%day% %hour%:%minute%:%second%

git commit -m "%commit_msg%"

git push || (echo Push failed. & exit /b 1)

echo Changes successfully pushed!

pause