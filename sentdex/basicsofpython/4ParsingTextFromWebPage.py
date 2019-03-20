import time
import urllib3
from urllib3 import connection_from_url
import datetime

website = 'https://stackoverflow.com/questions/47896461/get-shortest-path-to-a-cell-in-a-2d-array-python'
topsplit = '<div class="post-text" itemprop="text">'
bottomsplit = '</code></pre>'

def main():
    try:
        # urllib3.disable_warnings()
        http = urllib3.PoolManager()
        r = http.request('GET', website, preload_content=False)
        sourceCode = r.read()
        article = str(sourceCode).split(topsplit)[1].split(bottomsplit)[0]
        finalArticle = article.split('\\n')
        for line in finalArticle:
            if '<p>' in line:
                print(line)

    except Exception as e:
        print('failed')
        print(str(e))

main()