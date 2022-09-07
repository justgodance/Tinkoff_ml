#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[ ]:


def generate_random_sentence(length, dictionary):
    current_word = random.choice(list(dictionary.keys()))
    if type(current_word) == tuple:
        sentence = [str(item) for item in current_word]
    else:
        sentence = [current_word]
    if current_word == "":
        return sentence
    for i in range(0, length):
        current_dictogram = dictionary[current_word]
        random_word = random.choice(dictionary[current_word])
        current_word = random_word
        sentence.append(current_word)
    return sentence

