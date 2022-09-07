#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[ ]:


def generate_random_sentence(length, dictionary):
    k=1
    sentence = ()
    list2 = [item for item in list(dictionary.keys()) if len(item)==k]
    current_word = random.choice(list2)
    if current_word == "":
        return sentence
    sentence = [str(item) for item in current_word]
    for i in range(0, length):
        random_word = random.choice(dictionary[tuple(sentence)])
        current_word = random_word
        if current_word == "":
            return sentence
        sentence.append(current_word)
    return sentence

