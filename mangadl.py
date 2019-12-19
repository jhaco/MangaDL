import requests
import re
import os
import time
import concurrent.futures
import sys

#current works for: manganelo.com, mangakakalot.com

def chapter_list(site):
    page = requests.get(site)
    html = page.text
    pattern = re.compile(r'\s*a [^>]*href="([^"]+)')
    links = pattern.findall(html)

    name = site.rsplit("/", 1)[1]                                               #assumes name of comic is appended to end of url
    chapter_url = [ch for ch in links if name in ch]                            #assumes all chapter urls contains name of comic
    chapter_url.pop(0)                                                          #assumes "site" variable is included and always first on list
    return chapter_url

def dl_pages(site, directory):
    page = requests.get(site)
    if(page.ok):
        html = page.text
        pattern = re.compile(r'<\s*img [^>]*src="([^"]+)')                          
        img_url = pattern.findall(html)                                         #finds all html code for source images

        for img in img_url:
            #===================================================================
            filename = re.search(r'/([\w_-]+[.](jpg))$', img)                   #applies to jpg only; file type for comic pages; MODIFY FOR DIFFERENT IMAGE TYPE
            #===================================================================
            if filename is None:                                                #skips non-jpg image files i.e. headers, etc
                continue
            if(os.path.isfile(os.path.join(directory, filename.group(1)))):
                continue
            with open(os.path.join(directory, filename.group(1)), 'wb') as f:
                response = requests.get(img)                                    #requests img url, extracts image and writes to file
                f.write(response.content)
    else:
        print("Failed to get: " + site)

#===============================================================================

def dl_chapter(chapter, arc):                                                       
    name = chapter.split("/")[-1]                                               #assumes chapter number is appended at end of chapter url
    number = re.findall(r'[\d\.\d]+', name)                                     #removes all other non-numeric characters
    directory = os.path.dirname(os.path.realpath(__file__)) + '/archive/' + arc + '/' + number[-1]
    if not os.path.exists(directory):
        os.makedirs(directory)                                                  #generates folder for each chapter
        dl_pages(chapter, directory)                                             #only executes if chapter folder does not exist

#===============================================================================
if __name__ == '__main__':
    #site = input("Enter the site: ")
    site = sys.argv[1]
    #manga = input("Name the folder for this download: ")
    manga = sys.argv[2]

    start_time = time.time()

    chapters = chapter_list(site)
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as exec: #spreads processes across the number of available cores
        future_url = {exec.submit(dl_chapter, chapter, manga): chapter for chapter in chapters}
        for future in concurrent.futures.as_completed(future_url):
            try:
                future.result()
            except:
                print("Invalid URL")

    end_time = time.time()
    print("Elapsed time was %g seconds" % (end_time - start_time))
