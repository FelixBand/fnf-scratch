echo "If an older copy of the sb3 file already exists, it will be deleted."
pause

del "Friday Night Funkin'.sb3"

powershell -NoProfile -Command ^
    "& {Compress-Archive -Path 'Friday Night Funkin'\*' -DestinationPath 'Friday Night Funkin'.zip'}"

ren "Friday Night Funkin'.zip" "Friday Night Funkin'.sb3"

pause