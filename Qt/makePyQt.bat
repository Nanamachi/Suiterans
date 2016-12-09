echo off
set INPUT_FILE_NAME="mainwindow.ui"
set /P INPUT_FILE_NAME="plz write input file name -> "
set OUTPUT_FILE_NAME="mainwindow.py"
set /P OUTPUT_FILE_NAME="plz write output file name -> "
pyuic5 %INPUT_FILE_NAME% -o %OUTPUT_FILE_NAME%
