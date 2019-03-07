:: This script uses Nuitka to build an exe then deletes temp files

:: Turn echo off
@ECHO OFF

:: Set current directory
echo Setting up...
echo.
cd /D "%~dp0"

:: Get file from argument, set up command
set fileName=%1
set fileNameNoExt=%fileName:~0,-3%
set folderName=projects
cd ..
cd %folderName%
set toRun=python -m nuitka --standalone --mingw64 --show-progress %fileName%
::set toRun1=python setup.py install
::set toRun2=python setup.py py2exe

:: Set up a setup.py file for py2exe
::echo from distutils.core import setup>setup.py
::echo import py2exe>>setup.py
::echo setup(console=['%fileName%'])>>setup.py

:: Run command
echo Starting compilation...
echo.
::%toRun1%
::%toRun2%
%toRun%

:: Move exe outside to dist folder
echo Compilation complete.
echo.
echo Moving exe to main dist folder.
echo.
robocopy %fileName%.dist ../dist %fileNameNoExt%.exe /MOV

:: Delete temp files
echo Deleting temporary files...
echo.
rmdir /q /s %fileName%.build
rmdir /q /s %fileName%.dist

echo Complete.
echo.
pause