import time
import urllib3
from urllib3 import connection_from_url
import datetime


website = 'https://en.wikipedia.org/wiki/Sentiment_analysis'
myheaders = {'User-Agent':'Mozilla/5.0'}

opener = urllib3.HTTPConnectionPool

def main():
    try:
        # urllib3.disable_warnings()
        http = urllib3.PoolManager()
        r = http.request('GET', website, headers=myheaders, preload_content=False)
        sourceCode = r.read()

        finalArticle = str(sourceCode).split('\\n')
        for line in finalArticle:
            if '<p>' in line:
                print(line)

    except Exception as e:
        print('failed')
        print(str(e))

main()