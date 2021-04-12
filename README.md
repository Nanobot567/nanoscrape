# nanoscrape
a simple scraping program that can download webpages, discord embeds, and more.

## TOC

- [current capabilities](#current-capabilities)
- [run nanoscrape](#run-nanoscrape)
- [usage](#usage)


## current capabilities

- can download discord embed links
- can detect discord embed extension
- all file extensions are downloadable
- can download raw .html files

## run nanoscrape

### easier version

check if you have python installed by running `python --version` in command prompt or terminal for windows or mac os, respectively. __make sure that the version number is above 3.4.x if it shows a version number.__ if not, go [here](https://python.org/download) and download the latest python version. 

download and extract nanoscrape-main.zip and run nanoscrape.bat. this batch file runs the command `python nanoscrape.py` and starts up nanoscrape by itself.

### more complicated version (not recommended)
first, you need to have python installed on your computer. go [here](https://python.org/download) to download python.

- to check if you already have python installed, open command prompt on windows or terminal on mac os or linux and type `python --version`. if you see a version number, you have python installed. __make sure that the version number is above 3.4.x.__

once you have python installed, open command prompt or terminal.

navigate to the directory that nanoscrape is located, after you have downloaded and extracted the .zip (usually located in (username)\downloads\ on windows, or (username)/downloads/ on mac os)

type this command and press enter:

`python nanoscrape.py`

if you do not see an error, you are good to go!

------------

## usage

once you have runned nanoscrape, you should be greeted with this message:

```
Welcome to...


        nanoscrape.py
      version (version)
        


Please select an option.


1. Download from a discord link (insert extension)
2. Download from a discord link (detect extension)
3. Download from a direct download link
4. Show this menu
5. Quit 



NSCRAPE > 
```
- nanoscrape may say that you do not have pip installed. pip is a package manager used to get required modules in nanoscrape. to get pip, you can use a recent curl: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`. once you have installed pip, run `python get-pip.py` in command prompt or terminal. afterwards, you should be able to run nanoscrape fine.

from here, you can do 1 of 5 things:

```
1. Download from a discord link (insert extension)
2. Download from a discord link (detect extension)
3. Download from a direct download link
4. Show this menu
5. Quit 
```

each option is pretty self explainatory, but some examples of using these commands are:

1. (option 1): "i need to download a discord embed, and i know the file extension used."
2. (option 2): "i want to use this discord video in a memes channel, but i don't know the file extension."
3. (option 3): "i want to download this guide to read offline."
4. (option 4): "what are the options again?"
5. (option 5): "screw this, i'm leaving."
