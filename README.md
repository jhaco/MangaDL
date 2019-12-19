# MangaDL
A Python script to crawl a comic site and extract chapters. ~~Requires modifications to adapt to the specific links for each webpage.~~ The script will write files to a specified directory, and will place all images in their respective folder per chapter.

### Usage

* Input the URL of the primary comic page where all chapters are listed. Accounts for side chapters and main chapters.
  * Search for a comic you want to download from: https://manganelo.com
  * The link to input would look like this: https://manganelo.com/manga/peerless_dad
* Input name of folder. All downloaded chapters will be sent here.

### Plans

* to be planned

### Updates

* 12/19/2019 - Implemented batch scripting for greater ease of use and renamed some methods for consistency
* 12/03/2019 - Implemented automatic check for available cores for multi-processing; automatic file skip if files exists already, for ease of updating
* 12/02/2019 - Implemented multi-processing; reduced processing time from 10 chapters/minute to 100 chapters/minute; 571s to 83s
* 12/02/2019 - Modified for single input; less manual modifications 
* 11/30/2019 - First implementation.
