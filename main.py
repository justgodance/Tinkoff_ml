#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import os
import re
import sys
import train
import generate
import argparse


# In[ ]:


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", dest="order", required=True) #Сколько N
    parser.add_argument("--todo", dest="todo", required=True) #Генерация или обучение
    parser.add_argument("--length", dest="length", required=True) #Длина предложения
    parser.add_argument("--model", dest="model_path", required=True) #путь
    args = parser.parse_args()
    length = int(args.length)
    order = int(args.order)
    todo = str(args.todo)
    path = str(args.model_path)
    if todo == 'Train':
        dictionary = {}
        for file in os.listdir():
            if file.endswith('.txt'):
                file_path =f"{path}/{file}"
                dictionary = train.N_gram_model(dictionary,train.text_converter(file_path),order)
                dictionary[train.text_converter(file_path)[-1]] = ""
            with open('model.pkl', "w+b") as file:
                pickle.dump(dictionary, file) 
    if todo == 'Generate':
        with open('model.pkl', "rb") as f:
            dictionary = pickle.load(f)
        text = generate.generate_random_sentence(length,dictionary) # 5 - это длина
        print(*text)


# In[ ]:




