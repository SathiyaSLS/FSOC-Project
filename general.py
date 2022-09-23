#!/usr/bin/env python
# coding: utf-8

# In[26]:


import os
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import RPi.GPIO as GPIO


# In[27]:


def initPins(op = 14, ip = 15):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ip, GPIO.IN)
    GPIO.setup(op, GPIO.OUT)
    
def cleanup():
    initPins()
    GPIO.cleanup()


# In[28]:


def high(op = 14, t = 0.5):
    GPIO.output(op, GPIO.HIGH)
    time.sleep(t)


# In[29]:


def low(op = 14, t = 0.5):
    GPIO.output(op, GPIO.LOW)
    time.sleep(t)


# In[30]:


def read():
    pass


# In[31]:


initPins()
high()


# In[32]:


low()
cleanup()


# In[ ]:




