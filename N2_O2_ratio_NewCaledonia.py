# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:45:37 2024

@author: jdlpizerumug
"""

import matplotlib.pyplot as plt
import pandas as pd

dfdataNC= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                        sheet_name= "dataraw_ordered")   

O2_air= 20.95
N2_air= 78.08

# Data_ campaign2022
data22= dfdataNC[dfdataNC["Date"]=="May, 2022"]

# data by Type of sampled spring
Ophiolitic = data22[data22['Type'] == 'Ophiolitic']
Basement = data22[data22['Type'] == 'Basement']

#CREATING A SCATTER PLOT FOR N2/O2 CONCENTRATION
fig2, ax2 = plt.subplots()

ax2.scatter(Ophiolitic["IDss"], Ophiolitic["N2"]/Ophiolitic["O2"], marker= "D", color="forestgreen", s=50)
ax2.scatter(Basement["IDss"], Basement["N2"]/Basement["O2"], marker= "D", color="brown", s=50)

ax2.plot(data22["IDss"], ([N2_air/O2_air]*(len(data22["IDss"]))), color='black', linestyle="--")   #Air
# ax2.plot(data22["IDss"], ([0]*(len(data22["IDss"]))), color='grey', linestyle="-")   #Air

plt.ylim(-4, 25)

# Adding labels and title
ax2.set_xlabel('Samples', fontweight= "bold", fontsize= 13)
ax2.set_ylabel('$\mathbf{N_2/O_2}$', fontweight= "bold", fontsize= 13)

ax2.annotate("$\mathbf{N_2/O_2}$ of Air = 3.7", xy= (0, 2.2), xytext= (0,0), textcoords= "offset points", fontsize= 10, fontweight= "bold")

# Annotating figure number
plt.annotate("A", xy=(0, 24), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)

# saving the plot
plt.savefig("N2_O2_ratio_NewCaledonia.svg", format= "svg", bbox_inches='tight')

plt.show()