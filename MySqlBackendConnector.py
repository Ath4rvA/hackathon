#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 08:24:03 2020

@author: atharva
"""

    
from mysql import connector
import random
import matplotlib.pyplot as plt
import numpy as np


class mysqlbackend:
    def __init__(self,dbname,user,password):
        self.db=connector.connect(host="localhost",user=user,passwd=password,database=dbname)
        
    
    def top_4_field(self):
        cursor= self.db.cursor()
        query='''(select season, toss_winner, count(toss_winner) from matches
        where toss_decision="field" and season in (2016)
        group by season, toss_winner
        order by season desc, count(toss_winner) desc
        limit 4)
        UNION
        (select season, toss_winner, count(toss_winner) from matches
        where toss_decision="field" and season in (2017)
        group by season, toss_winner
        order by season desc, count(toss_winner) desc
        limit 4)
        
        '''
        teams=[]
        freq=[]
        cursor.execute(query)
        result= cursor.fetchall()
        for row in result:
            teams.append(row[1])
            freq.append(row[2])
            print("Year: ",row[0]," Team: ",row[1]," Count: ",row[2])
        cursor.close()
        N = 2
        #menMeans = (20, 35, 30, 35, 27)
        ##womenMeans = (25, 32, 34, 20, 25)
        #menStd = (2, 3, 4, 1, 2)
        #womenStd = (3, 5, 2, 3, 3)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        
        p1 = plt.bar(ind, teams, width)
        p2 = plt.bar(ind, freq, width,
                     bottom=teams)
        
        plt.ylabel('Scores')
        plt.title('Scores by group and gender')
        plt.xticks(ind, ('2016', '2017'))
        plt.yticks(np.arange(0, max(freq), 1))
        #plt.legend((p1[0], p2[0]), ('Men', 'Women'))
        
        plt.show()
        #plt.bar(teams,freq)
        #plt.show()
            
    def total_summary(self):
        cursor= self.db.cursor()
        query='''
        select t.season, t.batting_team, f.fours,s.sixes, t.total_runs from total_score t
        inner join fours f on f.batting_team=t.batting_team AND f.season=t.season
        inner join sixes s on s.batting_team=t.batting_team AND s.season=t.season
        order by t.season desc;
        '''
        cursor.execute(query)
        result= cursor.fetchall()
        for row in result:
            print("Year: ",row[0], " Team: ",row[1], " Fours: ",row[2]," Sixes: ",row[3]," Total Score: ",row[4])
        cursor.close()
        
    def top_ten_economy(self):
        cursor= self.db.cursor()
        query='''
        select T.season, T.bowler, T.economy from (select T.season, T.bowler, T.economy,
        row_number() over(partition by T.season order by T.economy asc) as rn
        from economy as T) as T
        where T.rn <= 10
        '''
        cursor.execute(query)
        result= cursor.fetchall()
        for row in result:
            print("Year: ",row[0], " Bowler: ",row[1]," Economy: ",row[2])
        cursor.close()
        
    def top_nrr_team(self):
        cursor= self.db.cursor()
        query='''
        SELECT season,team FROM v_nrr WHERE NET_RUN_RATE = ANY(SELECT MAX(NET_RUN_RATE) 
        FROM v_nrr GROUP BY SEASON) 
        ORDER BY SEASON;
        '''
        cursor.execute(query)
        result= cursor.fetchall()
        for row in result:
            print("Season: ",row[0]," Team: ",row[1])
        cursor.close()
        
    def top_april_team(self):
        cursor= self.db.cursor()
        query='''
        SELECT team FROM v_nrr WHERE NET_RUN_RATE = ANY(SELECT MAX(NET_RUN_RATE) FROM v_nrr 
        where month(date)=4 GROUP BY SEASON) ORDER BY NET_RUN_RATE DESC limit 1;
        '''
        cursor.execute(query)
        result= cursor.fetchall()
        for row in result:
            print("Team: ",row[0])
        cursor.close()