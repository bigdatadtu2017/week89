# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:14:55 2017

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

for row in c.execute('''WITH CTE AS
                        (
                        SELECT id, parent_id, subreddit_id, 0 as depth
                        FROM comments
                        UNION ALL
                        SELECT c.id, c.parent_id, c.subreddit_id, CTE.depth + 1
                        FROM comments AS c
                        INNER JOIN CTE 
                        ON c.parent_id = CTE.id
                        )
                        SELECT subreddit_id, avg(depth)
                        FROM CTE
                        GROUP BY subreddit_id
                        ORDER BY avg(depth) DESC
                        LIMIT 10
                        '''):
    print(row)
print('done')
end = time.time()
print('run time [s]:',end - start)
