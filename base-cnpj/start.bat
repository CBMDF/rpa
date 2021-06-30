@echo off

SET currentdir=%~dp0

pip install virtualenv

if not exist "env" (
   virtualenv env
)

call %currentdir%\env\Scripts\activate.bat

pip install -r requirements.txt
cls
python download.py

if "%ERRORLEVEL%"=="0" (
   call %currentdir%\init_pdi.bat
)
