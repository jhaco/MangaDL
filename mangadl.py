import requests
import re
import os
import time

def get_chapters(site):
    page = requests.get(site)
    html = page.text
    pattern = re.compile(r'\s*a [^>]*href="([^"]+)')
    links = pattern.findall(html)

    name = site.rsplit("/", 1)[1]                                           #assumes name of comic is appended to end of url
    chapter_url = [ch for ch in links if name in ch]                        #assumes all chapter urls contains name of comic
    chapter_url.pop(0)                                                      #assumes "site" variable is included and always first on list
    return chapter_url

def dl_page(site, directory):
    page = requests.get(site)
    html = page.text
    pattern = re.compile(r'<\s*img [^>]*src="([^"]+)')                          
    img_url = pattern.findall(html)                                         #finds all html code for source images

    for img in img_url:
        #===================================================================
        filename = re.search(r'/([\w_-]+[.](jpg))$', img)                   #applies to jpg only; file type for comic pages; MODIFY FOR DIFFERENT IMAGE TYPE
        #===================================================================
        if filename is None:                                                #skips non-jpg image files i.e. headers, etc
            continue
        with open(os.path.join(directory, filename.group(1)), 'wb') as f:
            response = requests.get(img)                                    #requests img url, extracts image and writes to file
            f.write(response.content)


#===========================================================================

start_time = time.time()

site = input("Enter the site: ")
chapters = get_chapters(site) 

for chap in chapters:                                                       
    name = chap.split("/")[-1]                                              #assumes chapter number is appended at end of chapter url
    number = re.findall(r'[\d\.\d]+', name)                                 #removes all other non-numeric characters
    directory = os.path.dirname(os.path.realpath(__file__)) + '/' + number[-1]
    if not os.path.exists(directory):
        os.makedirs(directory)                                              #generates folder for each chapter
    dl_page(chap, directory)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time)) 
