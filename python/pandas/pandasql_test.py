#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      : Hu Wenchao
Description : 对pandas dataframe执行SQL语句
'''
import pandas as pd
from pandasql import sqldf

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
            'age': [42, 52, 36, 24, 73],
            'preTestScore': [4, 24, 31, ".", "."],
            'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data,
                  columns=['first_name', 'last_name', 'age', 'preTestScore',
                           'postTestScore'])

print df

q = '''
SELECT sum(age),
       max(preTestScore),
       min(postTestScore)
FROM df
'''

print sqldf(q, globals())
