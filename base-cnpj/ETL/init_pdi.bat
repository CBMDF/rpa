@echo off

SET kitchen=C:\pentaho\data-integration\Kitchen.bat
SET currentdir=%~dp0
SET logfile="%currentdir%log.txt"

echo. >> %logfile%
echo. >> %logfile%

"%kitchen%" /file:"%currentdir%\job_cnpj.kjb" /level:Basic >> %logfile%