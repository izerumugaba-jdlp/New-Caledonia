# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:35:50 2025

@author: jdlpizerumug
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

dfdataNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                         sheet_name= "dataraw_ordered", index_col="IDss")
dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx", sheet_name="Serpent.Contexts", 
                         index_col="IDss")

# data by Type of sampled spring
Ophiolitic = dfdataNC[dfdataNC['Type'] == 'Ophiolitic']
Basement = dfdataNC[dfdataNC['Type'] == 'Basement']


#PLOTTING

# 36Ar vs 84Kr (Vacquand et al., 2018; Wang et al., 2022)
fig1, ax1 = plt.subplots()

ax1.scatter(Ophiolitic["36Ar"], Ophiolitic["84Kr"], marker= "D", color= "forestgreen", s=70, zorder= 5, label= "Ophiolitic (N.C)")
# ax1.scatter(Basement["36Ar"], Basement["84Kr"], marker= "D", color= "brown", s=70, zorder= 5, label= "Basement")


ax1.scatter(31.57*10**-6, 0.65*10**-6, marker= "*", color= "red", s=100) #Air
ax1.scatter(1.07*10**-6, 0.04*10**-6, marker= "*", color= "red", s=100) #ASW


# Literature_ Plotting
for country, color, label in [
    ("New Caledonia", "cornflowerblue", "NC (Literature))"),
    ("Oman", "grey", "Oman"),
    ("Philippines", "orange", "Philippines"),
    ("Turkey", "lightcoral", "Turkey")]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country
    ax1.scatter(
        dflitdata.loc[mask, "36Ar"],  # Filtered x-values
        dflitdata.loc[mask, "84Kr"],      # Filtered y-values
        marker="o", s=35, color=color, label=label, zorder= 4)

ax1.set_xlabel("$\mathbf{^{36}Ar}$ (g/g)", fontweight='bold', fontsize=13)
ax1.set_ylabel("$\mathbf{^{84}Kr}$ (g/g)", fontweight='bold', fontsize=13)
ax1.set_xlim(1e-07, 1e-03)
ax1.set_ylim(1e-09, 1e-04)
ax1.set_xscale('log') 
ax1.set_yscale('log')

# Setting both x and y axes to scientific notation
# ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3))

# ax1.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3))

# Annotating endmembers 
ax1.annotate("Air", xy= (4*10**-5, 7.5*10**-7), xytext= (0, 0), textcoords= "offset points", fontsize= 10, fontweight= "bold")
ax1.annotate("ASW", xy= (4*10**-7, 3*10**-8), xytext= (0, 0), textcoords= "offset points", fontsize= 10, fontweight= "bold")

plt.legend(loc= 'lower right')

# saving the figure
plt.savefig('36Ar_vs_84Kr_NewCaledonia.svg', format='svg', bbox_inches='tight')


plt.show()

