import requests
import re
import os
import time

def dl_page(site, directory):
    #for i in range(1, 100):
    #    filename = str(i) + '.jpg'
    #    response = requests.get(site + filename)
    #    if(response.ok):
    #        f = open(os.path.join(directory, filename), 'wb')
    #        f.write(response.content)
    #        f.close()
    #    else: 
    #        break
    
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

start_time = time.time()

for i in range(1,101):
    #site = 'https://s7.mkklcdnv7.com/mangakakalot/p1/peerless_dad/chapter_' + str(i) + '/'
    #=======================================================================
    site = 'https://manganelo.com/chapter/peerless_dad/chapter_' + str(i)   #MODIFY TO TAILOR TO THE WEBSITE
    #=======================================================================
    directory = os.path.dirname(os.path.realpath(__file__)) + '/' + str(i)
    if not os.path.exists(directory):
        os.makedirs(directory)                                              #generates folder for each chapter
    dl_page(site, directory)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time)) 