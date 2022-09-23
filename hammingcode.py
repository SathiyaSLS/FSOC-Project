#!/usr/bin/env python
# coding: utf-8

# # Forward Error Correction Codes
# ### Miscellaneous Functions

# In[ ]:


def evenParityGen(p):
    if (p % 2 == 0):
        return "0"
    else:
        return "1"


# In[ ]:


def evenParityChk(a, b, c, d):
    if ((int(a) + int(b) + int(c) + int(d)) % 2) == 0:
        return "0"
    else:
        return "1"


# In[ ]:


def bitCheck(data1, data2):
    error = 0
    if len(data1) == len(data2):
        for i in range(len(data1)):
            if data1[i] != data2[i]:
                error += 1
        return error
    else:
        raise ValueError("Two arguments ({},{}) must be same length".format(
            data1, data2))


# ## Hamming Error Correction Code

# In[ ]:


#AB0C123
def hammingEnc(data):
    if len(data) == 4:
        pA = int(data[0]) + int(data[1]) + int(data[3])
        pA = evenParityGen(pA)
        pB = int(data[0]) + int(data[2]) + int(data[3])
        pB = evenParityGen(pB)
        pC = int(data[1]) + int(data[2]) + int(data[3])
        pC = evenParityGen(pC)
    else:
        raise ValueError("Data '{}' Should be bitlength of 4".format(data))
    data = pA + pB + data[0] + pC + data[1] + data[2] + data[3]
    return data


# In[ ]:


#AB0C123
#0123456
def hammingDec(data):
    pos = {  #Dictionary for error numbers. (Numbers are one less than actual because of array indexing)
        "000": None,
        "001": 0,
        "010": 1,
        "011": 2,
        "100": 3,
        "101": 4,
        "110": 5,
        "111": 6
    }
    if len(data) == 7:
        eC = evenParityChk(data[0], data[2], data[4], data[6])
        eB = evenParityChk(data[1], data[2], data[5], data[6])
        eA = evenParityChk(data[3], data[4], data[5], data[6])
        pstn = pos[eA + eB + eC]
        if pstn != None:
            if (data[pstn] == "0"):
                data = data[:(pstn)] + "1" + data[(pstn + 1):]
            else:
                data = data[:(pstn)] + "0" + data[(pstn + 1):]
        newdata = data[2] + data[4] + data[5] + data[6]
    else:
        raise ValueError("Data {} should have bitlength of 7".format(data))
    if bitCheck(data, hammingEnc(newdata)) <= 1:
        return newdata
    else:
        return "XXXX"


# #### Hamming Code - For Full Data

# In[ ]:


def hamEnc(data):
    rtndata = ''
    byte = ''
    count = 0
    for i in range(len(data) + 1):
        if ((count != 0) & (count % 4 == 0)):
            rtndata += hammingEnc(byte)
            byte = ''

        if (i != len(data)):
            byte += data[i]
        else:
            byte = ''

        count += 1
    return rtndata


# In[ ]:


def hamDec(data):
    rtndata = ''
    byte = ''
    count = 0
    for i in range(len(data) + 1):
        if ((count != 0) & (count % 7 == 0)):
            rtndata += hammingDec(byte)
            byte = ''

        if (i != len(data)):
            byte += data[i]
        else:
            byte = ''

        count += 1
    return rtndata


# ## Repeative Error Correction Code

# In[ ]:


def repeatEnc(data,i = 3):
    data = i*data
    return data


# In[ ]:


def repeatDec(data):
    count0 = 0
    count1 = 0
    for i in data:
        if i == "0":
            count0 += 1
        else:
            count1 += 1
    if (count0 > count1):
        return "0"
    else:
        return "1"

