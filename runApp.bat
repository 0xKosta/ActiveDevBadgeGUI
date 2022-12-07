Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Batch Files\syncfiles.bat" & Chr(34), 0
Set WshShell = Nothing
@echo off

echo Starting setup...
echo Installing hikari...
pip install hikari
echo Hikari installed!
echo Installing lightbulb...
pip install hikari-lightbulb
echo Lightbulb installed
echo Installing customtkinter...
pip install customtkinter
echo customtkinter installed
echo All requirements met, starting the program.
python main.py