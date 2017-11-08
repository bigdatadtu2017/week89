# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:07:11 2017

@author: andre
"""

import sqlite3 # import packages
import time
import re

start = time.time()
# upload data
dataSQL = sqlite3.connect('reddit.db')
dataSQL.text_factory = bytes
c = dataSQL.cursor()

n = 10
topn_names = [None]*n
topn_counts = [0]*n

for row in c.execute('''SELECT subreddit_id, GROUP_CONCAT(body) 
                         FROM
                             (SELECT *
                              FROM comments
                              GROUP BY id
                              ORDER BY id 
                              )
                         GROUP BY subreddit_id
                         ORDER BY subreddit_id 
                         '''):
    name = str(row[0])
    count = len(set(re.findall('\w+', str(row[1]).lower())))
    if count > min(topn_counts):
        topn_names[topn_counts.index(min(topn_counts))] = name
        topn_counts[topn_counts.index(min(topn_counts))] = count

list1, list2 = zip(*sorted(zip(topn_counts,topn_names), reverse = True))

print(list1)
print(list2)
print('done')
end = time.time()
print(end - start)

#%%