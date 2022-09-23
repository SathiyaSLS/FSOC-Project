#!/usr/bin/env python
# coding: utf-8

# # Code to convert Any file to binary of 0s and 1s

# In[1]:


from general2 import *
from hammingcode import *


def readFile(dir):
    with open(dir, "rb") as f:
        data = f.read()
    return data

def flnameconv(flname):
    flnamebin = ''
    for i in flname:
        flnamebin += format(ord(i), '08b')
    flnamebin += '0011101011111111101010101111111100111010'  # separate file name with data by charactes :ÿªÿ:
    return flnamebin

def writeFile(dir,data):
    with open(dir, "w") as f:
        f.write(data)


# In[2]:


def encoding(data, method):
    enc_data_bin = ''
    byte = ''
    count = 0
    
    if (method == "hamming"):
        for i in range(len(data) + 1):
            if ((count != 0) & (count % 4 == 0)):
                enc_data_bin += hammingEnc(byte)
                byte = ''

            if (i != len(data)):
                byte += data[i]
            else:
                byte = ''
            count += 1
    
    elif (method == "repeat"):
        for i in data:
            enc_data_bin += repeatEnc(i)
    
    elif (method == "none"):
        enc_data_bin = data
            
    return enc_data_bin


# In[12]:


def file2Binary(dir, encode = "repeat", encode2 = "none"):
    
    ext_bin = ''
    
    src_data = readFile(dir)
    src_data_bin = ''.join(format(i, '08b') for i in src_data)
    
#     print(src_data,src_data_bin, len(src_data), len(src_data_bin))
    
    # THIS BLOCK WILL ADD 128bits FOR EXTENSION AND THEN FILENAME TO IT SEPERATED BY :ÿªÿ:
    ext = os.path.splitext(dir)[1]
    for i in ext:
        ext_bin += format(ord(i), '08b')
    for i in range(16 - len(ext)):
        ext_bin += '00000000'
    filename_bin = flnameconv(os.path.split(os.path.splitext(dir)[0])[1])
    src_data_bin = ext_bin + filename_bin + src_data_bin
    
    encoded_data = encoding(src_data_bin, encode)
    second_encoded_data = encoding(encoded_data, encode2)
    
    enc_bin_dir = (os.path.dirname(dir) + "/" +os.path.split(os.path.splitext(dir)[0])[1] +"_FEC_binary.txt")
    print(enc_bin_dir)
    writeFile(enc_bin_dir,second_encoded_data)
    
    return second_encoded_data


# In[13]:


# file2Binary("/home/Pi_SLS_Tx/Project/10letters.txt",'none','none')


# In[ ]:





# In[ ]:




