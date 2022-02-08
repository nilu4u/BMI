#!/usr/bin/env python
# coding: utf-8

# In[40]:


import json
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')


# In[41]:


def BMI_table(bmi):
    bmi_category = ''
    health_risk = ''
    bmi_table = dict()
    if bmi<=18.4:
        bmi_category="Underweight", 
        health_risk="Malnutrition risk"
    elif bmi>=18.5 and bmi<=24.9:
        bmi_category= "Normal weight"
        health_risk="Low risk"
    elif bmi>=25 and bmi<=29.9:
        bmi_category="Overwight"
        health_risk="Enhanced risk"
    elif bmi>=30 and bmi<=34.9:
        bmi_category="Moderately obese"
        health_risk="Medium risk"
    elif bmi>=35 and bmi<=39.9:
        bmi_category="Severely obese"
        health_risk="High risk"
    else:
        bmi_category="Very severely obese"
        health_risk="Very high risk"
    return str(bmi_category) + ',' + str(health_risk)


# In[42]:


def BMI_calc(file_name):
    if not (os.path.exists(file_name)):
        print('file dosent exists')
        return
    df = pd.read_json(file_name)
    df['BMI'] = df['WeightKg']/(df['HeightCm']*0.01)
    df[['BMI Category','Health risk']] = df['BMI'].apply(BMI_table).apply(lambda x: x.split(',')).tolist()
    over = df[df['BMI Category']=='Overweight'].shape[0]
    print('Number of obese {}'.format(over))
    json_file = df.to_json(orient='columns')
    with open('Output.json','w') as f:
        f.write(json_file)
    print('Output file written as Output.json')


# In[ ]:




