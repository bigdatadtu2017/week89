# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:21:46 2017

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

for row in c.execute('''SELECT a.subreddit_id, b.subreddit_id, COUNT(*) AS common_authors   --#Output
                        FROM
                            (SELECT DISTINCT subreddit_id, author_ID                        --#Inner loop, selecting            
                              FROM comments                                                 
                              ORDER BY id 
                              ) a                                                           --#temporary structure, a
                        JOIN
                            (SELECT DISTINCT subreddit_id, author_ID
                              FROM comments
                              ORDER BY id 
                              ) b                                                           --#temporary stucture b
                        ON a.author_ID = b.author_ID                                        --#joins with it self
                        WHERE a.subreddit_id <> b.subreddit_id                              --#where subreddit_id's are not equal. 
                        GROUP BY a.subreddit_id, b.subreddit_id                             --#groups
                        ORDER BY COUNT(*) DESC                                              --#descending, oder by counts of group
                        LIMIT 20 '''):                                                      #top 10 subreddit pairs
    print(row)
print('done')
end = time.time()
print('run time [s]:'end - start)
