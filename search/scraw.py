# -*- coding: utf-8 -*-
import re
import string
import urllib
import urllib2
from StringIO import StringIO
import gzip
import json


def scraw_data():
    print "start"
    url = 'https://www.semanticscholar.org/api/1/search'

    user_agent = 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    new_file=open("../data/literature_data.txt",'w+')
    for i in range(100,500):
        print i
        values={
            "queryString":"video search",
            "page":i,
            "pageSize":10,
            "sort":"relevance",
            "authors":[],
            "classifications":[],
            "coAuthors":[],
            "dataSets":[],
            "keyPhrases":[],
            "venues":[]
        }

        headers = { 'User-Agent' : user_agent,
                    'Accept':'application/json',
                    'Accept-Encoding':'gzip, deflate',
                    'Content-Type':'application/json'
                    }

        data = json.dumps(values)

        req = urllib2.Request(url,data,headers)
        response = urllib2.urlopen(req)
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()

        result=json.loads(data)
        literatures=result['results']

        for l in literatures:
            id=l['id']
            title=l['title']['text']
            authors=l['authors']
            year=l['year']
            new_file.write(json.dumps({'id':id,'title':title,"authors":authors,'year':year})+'\n')
    new_file.close()
scraw_data()