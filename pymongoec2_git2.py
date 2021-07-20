#!/usr/bin/env python
# coding: utf-8

# In[10]:


#from flask import *
import pymongo
from pymongo import MongoClient


# In[11]:


Client=MongoClient("localhost",27017)


# In[12]:


Client.list_database_names()     


# In[13]:


db=Client.bookdb


# In[14]:


db.list_collection_names()   


# In[15]:


db.products.find() 


# In[16]:


from pprint import pprint


# In[18]:


import pandas as pd 
CM = [data for data in db.products.find()]
df_CM = pd.DataFrame(CM)
pprint(df_CM)


# In[ ]:




