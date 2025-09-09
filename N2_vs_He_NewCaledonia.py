# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 17:48:00 2025

@author: jdlpizerumug
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D

# Importing readyfiles
dfdataNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                         sheet_name= "dataraw_ordered", index_col="IDss")


plt.figure(figsize=(4, 5))
 
# Data Plotting
# Plot Ophiolitic samples
ophiolitic = dfdataNC[dfdataNC["Type"] == "Ophiolitic"]
plt.scatter(ophiolitic["N2"], ophiolitic["4He"], marker="s", color="forestgreen", s=70, label="4He Ophiolitic", zorder=5)
plt.scatter(ophiolitic["N2"], ophiolitic["3He"], marker="o", color="forestgreen", s=70, label="3He Ophiolitic", zorder=5)

# Plot Basement samples
basement = dfdataNC[dfdataNC["Type"] == "Basement"]
plt.scatter(basement["N2"], basement["4He"], marker="s", color="brown", s=70, label="4He Basement", zorder=5)
plt.scatter(basement["N2"], basement["3He"], marker="o", color="brown", s=70, label="3He Basement", zorder=5)




for i in dfdataNC.index:
                    
    
    if i in ["Cr"]:
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"3He"]), 
                        xytext=(10, -1), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"4He"]), 
                        xytext=(10, -1), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
        
    elif i in ["Co1B"]:
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"3He"]), 
                        xytext=(-6, -3), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"4He"]), 
                        xytext=(-6, -3), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
    elif i in ["Mo"]:
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"3He"]), 
                        xytext=(-6, -3), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"4He"]), 
                        xytext=(-6, -3), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
    else:
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"3He"]), 
                        xytext=(2, -6), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
        plt.annotate(dfdataNC.loc[i,"IDCs"], xy=(dfdataNC.loc[i,"N2"], dfdataNC.loc[i,"4He"]), 
                        xytext=(0, 16), ha='center', va='top', textcoords='offset points', fontsize= 12, zorder=6)
    
                    
    
# Labels and formatting
plt.xlabel("$\mathbf{N_2}$ (mol %)", fontweight="bold", fontsize= 13)
plt.ylabel("He (g/g)", fontweight="bold", fontsize= 13)
plt.yscale('log')
plt.xlim(0, 100)
plt.ylim(1e-12, 1e-03)

# Custom legend
legend_elements = [
    Line2D([0], [0], marker='s', linestyle='None', markerfacecolor='white', markeredgecolor='black', label='4He', markersize=9),
    Line2D([0], [0], marker='o', linestyle='None', markerfacecolor='white', markeredgecolor='black', label='3He', markersize=9),
    Line2D([0], [0], marker='D', linestyle='None', markerfacecolor='forestgreen', markeredgecolor='none', label='Ophiolitic', markersize=9),
    Line2D([0], [0], marker='D', linestyle='None', markerfacecolor='brown', markeredgecolor='none', label='Basement', markersize=9),
]

plt.legend(handles=legend_elements, fontsize=11, loc='lower left')

# Annotating figure number
plt.annotate("B", xy=(7, 5e-04), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 22, fontweight= "bold", zorder=6)

ax = plt.gca()
# Setting locator: Major ticks every 2 units on x-axis
# ax.xaxis.set_major_locator(ticker.MultipleLocator(2))

# Setting formatter: Use scientific notation without offset
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.1e}"))


plt.savefig('N2_vs_He_NewCaledonia.svg', format='svg', bbox_inches='tight')
plt.show()