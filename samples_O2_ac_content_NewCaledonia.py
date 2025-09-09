# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:45:37 2024

@author: jdlpizerumug
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dfdataNC= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Gasdata_NC_AirCorrected.xlsx") 

data22= dfdataNC[dfdataNC["Date"]=="May, 2022"]  

# data by Type of sampled spring
Ophiolitic = data22[data22['Type'] == 'Ophiolitic']
Basement = data22[data22['Type'] == 'Basement']

# Creating a scatter plot
fig, ax = plt.subplots()
ax.scatter(Ophiolitic["IDs"], Ophiolitic["O2"], marker= "D", s= 50, color="forestgreen", label= "Ophiolitic")
ax.scatter(Basement["IDs"], Basement["O2"], marker= "D", s= 50, color="brown", label= "Basement")

plt.plot(data22["IDs"], ([0]*11), "k--")   #Air

plt.ylim(-4, 100)

# Adding labels and title
plt.xlabel('Samples', fontweight= "bold", fontsize= 13)
plt.ylabel('$\mathbf{[O_2]}$ - air-corrected (%)', fontweight= "bold", fontsize= 13)

plt.legend(loc= "best", fontsize= 12, handletextpad=0.00001)
# plt.yscale("log")
# plt.title()


# Annotating a specific point, e.g., the third point
# ax.annotate('Air= 0‰', xy=(dfdataNC.loc[5, "IDs"], 1), xytext=(dfdataNC.loc[5, "IDs"], 0.7), color= "black")

# Annotating figure number
plt.annotate("B", xy=(0, 96), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)

# Show the plot
plt.savefig("samples_O2_content_ac.svg", format= "svg", bbox_inches='tight')
plt.show()