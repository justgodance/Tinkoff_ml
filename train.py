#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pickle
import os
import re
import sys
import random


# In[92]:


def text_converter(filepath):
    text = ""
    with open(filepath, "r",encoding='utf-8') as file:
        for line in file.readlines():
            if line != '\n':
                text += line
    text = text.lower()
    text = re.sub(r'[^a-z0-9а-яё\s]', '', text)
    text = re.sub(r'\n', ' ', text)
    text = text.split()
    return text


# In[93]:


def training_update(dictionary, text, window):
    list = dictionary[window]
    for item in text:
        list.append(item)
    return list


# In[94]:


def training(text):
    list = []
    for item in text:
        list.append(item)
    return list    


# In[139]:


def N_gram_model(dictionary, text, order):
    for j in range(1,order+1):
        for i in range(len(text)-j):
            window = tuple(text[i: i+j])
            if window in dictionary:
                dictionary[window] = training_update(dictionary, [text[i+j]], window)
            else:
                dictionary[window] = training([text[i+j]])
    return dictionary


# In[ ]:





# In[ ]:





# In[ ]:




