# -*- coding: utf-8 -*-
from model import recommend,Literature

class run :

    def __init__(self):
        self.run = recommend()
        self.run.read_from_file('data/literature_data.txt')

        self.result=list()


    def get_recommend(self,literature):
        result=[]
        for l in self.run.literatures:
            result.append(self.run.cos_similarity(literature,l.title))
        result.sort(reverse=True)
        return result










