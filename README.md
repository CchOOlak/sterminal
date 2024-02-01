# STerminal

This is a simple terminal written using *PyQT5* and can be executed on windows using *PyInstaller*.

## Install

    pip install -r requirements.txt

## Run 

    python app.py

## Build

to build executable files, you can run command below to get your executable file under `./dist` folder:

    pyinstaller --onefile --windowed app.py

now you can run `app.exe` as `administrator` to access all files and folders on your windows.