#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install -U googlemaps')


# In[2]:


import googlemaps
import pandas as pd
from datetime import datetime


# In[3]:


gmaps = googlemaps.Client(key='AIzaSyANTL4fK3H0IHuKxQK2A2FXPXi438XuxRU')


# In[4]:


dados = pd.read_table('teste.csv', sep = ';')


# In[5]:


dados


# In[6]:


colrotas=[]
for i in range(20):
    Origem = "\""+ dados['Origem'].iloc[i]+"\""
    Destino = "\""+ dados['Destino'].iloc[i]+"\""
    resultado = gmaps.directions(Origem, Destino , mode="transit")
    rota = []
    try:
        for etapa in resultado[0]['legs'][0]['steps']:
            if etapa['travel_mode'] == 'TRANSIT':
                rota.append(etapa['transit_details']['line']['short_name'])
        
    except IndexError:
        rota=[]
    colrotas.append(rota)


# In[7]:


import numpy as np
myarray = np.array(colrotas, dtype = list)
dados['Rotas'] = myarray


# In[8]:


dados


# In[ ]:




