from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

bsObject = BeautifulSoup(source, 'lxml')

csvFile = open('scrap.csv', 'w')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['headline', 'summary', 'video_link'])

for article in bsObject.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        videoSource = article.find('iframe', class_='youtube-player')['src']
        videoId = videoSource.split('/')[4]
        videoId = videoId.split('?')[0]
        ytLink = f'https://www.youtube.com/watch?v={videoId}'
    except Exception as e:
        ytLink = None

    print(ytLink)
    print()

    csvWriter.writerow([headline, summary, ytLink])

csvFile.close()
