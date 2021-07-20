#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import *
import pymongo
from pymongo import MongoClient


# In[2]:


Client=MongoClient("localhost",27017)


# In[3]:


Client.list_database_names()     


# In[4]:


db=Client.bookdb


# In[5]:


db.list_collection_names()   


# In[6]:


db.products.find() 


# In[7]:


from pprint import pprint


# In[9]:


import pandas as pd 
CM = [data for data in db.products.find()]
df_CM = pd.DataFrame(CM)
pprint(df_CM)


# In[ ]:




