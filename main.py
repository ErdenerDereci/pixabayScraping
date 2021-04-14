from selenium import webdriver
from urlextract import URLExtract
import time
import urllib.request
import numpy as np
from tqdm import tqdm
from bs4 import BeautifulSoup
sleeps = [1,0.5,1.5,0.7]
imagelist = set([])
DRIVER_PATH = "C:\\Users\\x\\Desktop\\chromedriver"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
def downloadImages(page):

    for i in range(1,page):
        print(i)
        driver.get("view-source:https://pixabay.com/images/search/orchid%20flower/?pagi="+str(i))
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        urls = soup.findAll("span", {"class": "html-attribute-value"})
        extractor = URLExtract()

        a = 0

        for url in urls:
            extractedUrls = extractor.find_urls(url.text)
            for extUrl in extractedUrls:
                if ".jpg" in extUrl or ".png" in extUrl:
                    a += 1
                    imagelist.add(extUrl)

        for x in imagelist:
            print(x)

        print("----------------------------")
        print(len(imagelist))
        time.sleep(3)

downloadImages(10)
for i, link in enumerate(tqdm(imagelist)):
    if link is not None:
        name = "orchidFlower" + f'{i}.jpeg'
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'whatever')
        filename, headers = opener.retrieve(link, name)
        time.sleep(np.random.choice(sleeps))

driver.quit()


