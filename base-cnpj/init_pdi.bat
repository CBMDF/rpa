SET kitchen=C:\pentaho\data-integration\Kitchen.bat
SET currentdir=%~dp0

"%kitchen%" /file:"%currentdir%\etl\job-base-cnpj.kjb" /level:Basic

pause