#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')


# reading the database
data = pd.read_csv("D:\Data Analysis\PYTHON WORK\LinkedInData\\Invitations.csv")

# printing the top 500 rows
display(data.head(500))


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt


# reading the database
data = pd.read_csv("D:\Data Analysis\PYTHON WORK\LinkedInData\\Invitations.csv")

# Scatter plot with day against tip
plt.plot(data['From'])
plt.plot(data['To'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Sent At')
plt.ylabel('From')

plt.show()


# In[ ]:




