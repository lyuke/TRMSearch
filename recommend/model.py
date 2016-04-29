# -*- coding: utf-8 -*-
import json
import codecs
from math import sqrt
stoping_words=('a','an','the','and','of','if','else')
class Literature:
    def __init__(self):
        self.title=''
        self.authors=[]
        self.year=''
        self.id=''

    def from_json(self,data):
        temp=json.loads(data)
        self.title=temp['title']
        self.id=temp['id']
        self.year=temp['year']['text']
        for author in temp['authors']:
            self.authors.append(author['text'])


class recommend:

    def __init__(self):
        self.literatures=[]

    def read_from_file(self,filename):
        file=open(filename,'r')
        for line in file:
            literature=Literature()
            literature.from_json(line)
            self.literatures.append(literature)




    def pearson(self, rating1, rating2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        for key in rating1:
            if key in rating2:
                n += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        if n == 0:
            return 0
        # 计算分母
        denominator = (sqrt(sum_x2 - pow(sum_x, 2) / n)
                       * sqrt(sum_y2 - pow(sum_y, 2) / n))
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / n) / denominator


    def recommend(self,username, users):
        """返回推荐结果列表"""
        # 找到距离最近的用户
        nearest = self.computeNearestNeighbor(username, users)[0][1]
        recommendations = []
        # 找出这位用户评价过、但自己未曾评价的乐队
        neighborRatings = users[nearest]
        userRatings = users[username]
        for artist in neighborRatings:
            if not artist in userRatings:
                recommendations.append((artist, neighborRatings[artist]))
        # 按照评分进行排序
        return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

    def computeNearestNeighbor(self,username, users):
        """计算所有用户至username用户的距离，倒序排列并返回结果列表"""
        distances = []
        for user in users:
            if user != username:
                distance = self.manhattan(users[user], users[username])
                distances.append((distance, user))
        # 按距离排序——距离近的排在前面
        distances.sort()
        return distances

    def manhattan(self,rating1, rating2):
        """计算曼哈顿距离。rating1和rating2参数中存储的数据格式均为
        {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
        distance = 0
        for key in rating1:
            if key in rating2:
                distance += abs(rating1[key] - rating2[key])
        return distance

    def cos_similarity(self,literature1,literature2):
        words=set()
        vector1 =list()
        vector2 = list()
        temp_words1=literature1.split()
        temp_words2=literature2.split()
        for w in stoping_words:
            if w in temp_words1:
                temp_words1.remove(w)
            if w in temp_words2:
                temp_words2.remove(w)
        for w in temp_words1:
            words.add(w)
        for w in temp_words2:
            words.add(w)
        for word in words:
            if word in literature1:
                vector1.append(1)
            else:
                vector1.append(0)
            if word in literature2:
                vector2.append(1)
            else:
                vector2.append(0)

        return self.cal_cos(vector1,vector2)




    def cal_cos(self,list1,list2):
        sum_x=0
        sum_y=0
        sum_x2=0
        sum_y2=0
        sum_xy=0
        for i in range(0,len(list1)):
            sum_x+=pow(list1[i],2)
            sum_y+=pow(list2[i],2)
            sum_xy+=list1[i]*list2[i]
        sum_x2=sqrt(sum_x)
        sum_y2=sqrt(sum_y)
        return sum_xy/(sum_x2*sum_y2)



