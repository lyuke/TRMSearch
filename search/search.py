# -*- coding: utf-8 -*-
import re
import string
import urllib
import urllib2
from StringIO import StringIO
import gzip
import json



_dict_index={}

def create_inverted_index(filename):
    print("读取文件%r"%filename)
    file=open(filename,'r')
    for line in file:
        literature=json.loads(line)
        # print literature['title']
        line_words=literature['title'].split()
        for word in line_words:
            if word not in _dict_index:
                item=set()
                item.add(literature['id'])
                _dict_index[word]=item
            else:
                _dict_index[word].add(literature['id'])


create_inverted_index('../data/literature_data.txt')

word_list = _dict_index.items()
word_list.sort( key = lambda items : items[0] )
for word , row in word_list :
    list_row = list(row)
    list_row.sort()
    for i in range ( 0 , len(list_row) ):
        list_row[i] = str(list_row[i])


    print word + ':' , ', '.join(list_row)


query_list = []

while True:
    print "请输入搜索的文献标题"
    query = raw_input()
    if query == '' :
        break
    elif len(query) != 0 :
        query_list.append(query) # append query inputed to a list query_list .


def judger(_dict , query):
    list_query = query.split()
    for word in list_query :
        if word in _dict :
            return 1
    return 0


def query():

    for list_query in query_list :
        if judger(_dict_index , list_query) == 0 :
            print 'None'
        else:
            list_query = list_query.split()
            query_set = set()
            for isquery in list_query :
                query_set = query_set | _dict_index[isquery]
            for isquery in list_query :
                query_set = query_set & _dict_index[isquery]
            if len(query_set) == 0 :
                print 'None'
            else:
                query_result = list(query_set)
                query_result.sort()
                for m in range(len(query_result)) :
                    query_result[m] = str(query_result[m])

                print ', '.join(query_result)

query()