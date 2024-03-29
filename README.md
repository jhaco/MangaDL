# MangaDL
A Python script to crawl a comic site and extract chapters. The script will write files to a specified directory, and will place all images in their respective folder per chapter. 

Currently only works for the following websites: manganelo, mangakakalot 

### Usage

* Ensure both mangadl.py and run_mangadl.bat are in the same directory.
* Find the comic to download (example: https://manganelo.com/manga/peerless_dad)
* Edit the batch file and add two arguments: the website and the folder name.
* For every comic to download, call another python line (sample below).
* ECHO are optional (for debugging purposes).
* Click and run the batch file.

```batch
@ECHO OFF

python "%~dp0\mangadl.py" "website1" "folder1"
ECHO completed: comic1 & ECHO.

python "%~dp0\mangadl.py" "website2" "folder2"
ECHO completed: comic2 & ECHO.

PAUSE
```

### Plans

* check a folder if it has no files

### Updates

* 12/19/2019 - Implemented batch scripting for repeated ease of use and renamed some methods for visual consistency
* 12/19/2019 - Modified a line to skip folders that already exist for faster updates
* 12/03/2019 - Implemented automatic check for available cores for multi-processing; automatic file skip if files exists already, for ease of updating
* 12/02/2019 - Implemented multi-processing; reduced processing time from 10 chapters/minute to 100 chapters/minute; 571s to 83s
* 12/02/2019 - Modified for single input; less manual modifications 
* 11/30/2019 - First implementation.
