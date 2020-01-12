:: This script uses Pyinstaller to build an exe then deletes temp files
:: Run this from a command prompt,
::   using the name of the file as the argument (no extension)
:: Example: ./compile-win.cmd CoinFlip

:: Turn echo off
@ECHO OFF

:: Set current directory
echo Setting up...
echo.
cd /D "%~dp0"

:: Get file from argument, set up command
set fileName=%1
set folderName=projects
cd ..
cd %folderName%
set toRun=pyinstaller -F %fileName%.py

:: Run command
echo Starting compilation...
echo.
%toRun%

:: Move exe outside to dist folder
echo Compilation complete.
echo.
echo Moving exe to main dist folder.
echo.
robocopy dist ../dist/%fileName% %fileName%.exe /MOV

:: Delete temp files
echo Deleting temporary files...
echo.
rmdir /q /s __pycache__
rmdir /q /s build
rmdir /q /s dist
del /q /s %fileName%.spec

echo Complete.
echo.
pause