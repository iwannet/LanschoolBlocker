@echo off
msg * "Credits to iwannet" 
msg * "Enter The Path to Your exe !!Without quotes!!"
set /p input=
if %input% == 1 goto ech
:ech
echo Typ enter to install ;
echo %input%
pause



set _COMPAT_LAYER=RunAsInvoker
 
Start %input%
