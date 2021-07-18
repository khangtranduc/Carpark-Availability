@echo off
:loop

python C:\Users\Owner\Desktop\data_collection.py

echo Ooopsiee !!!

timeout /T 790 /NOBREAK > nul
goto loop
pause