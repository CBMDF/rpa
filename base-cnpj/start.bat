SET currentdir=%~dp0

call %currentdir%\env\Scripts\activate.bat
python download_files.py

if "%ERRORLEVEL%"=="0" (
   call %currentdir%\pentaho.bat
)