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

for row in c.execute('''SELECT a.subreddit_id, b.subreddit_id, COUNT(*) AS common_authors
                        FROM
                            (SELECT DISTINCT subreddit_id, author_ID
                              FROM comments
                              ORDER BY id 
                              LIMIT 60000000) a
                        JOIN
                            (SELECT DISTINCT subreddit_id, author_ID
                              FROM comments
                              ORDER BY id 
                              LIMIT 60000000) b
                        ON a.author_ID = b.author_ID
                        WHERE a.subreddit_id <> b.subreddit_id 
                        GROUP BY a.subreddit_id, b.subreddit_id
                        ORDER BY COUNT(*) DESC 
                        LIMIT 1 '''):
    print(row)
print('done')
end = time.time()
print(end - start)