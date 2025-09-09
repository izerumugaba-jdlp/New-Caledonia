# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:38:42 2025

@author: jdlpizerumug
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import FancyArrowPatch


# As presented in Deville and Prinzhofer (2016)
dfdataNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Waterchemistry_Physicochempar.xlsx",
                         sheet_name= "data_og", index_col="IDCs")
dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx", sheet_name="Serpent.Contexts_plot", 
                         index_col="IDss")

# PLOTTING
fig, ax = plt.subplots()

# Grids
plt.grid(True, linestyle='--', linewidth=0.4)

# data_this study
# data
dfdataNC_South = dfdataNC[dfdataNC['Zone'] == 'South']
dfdataNC_North = dfdataNC[dfdataNC['Zone'] == 'North']

ax.scatter(dfdataNC_South.loc[:,"pH"], dfdataNC_South.loc[:,"Eh_mV"], marker= "D", color= "forestgreen", s=80, zorder= 5, label= "Ophiolitic Sites")
ax.scatter(dfdataNC_North.loc[:,"pH"], dfdataNC_North.loc[:,"Eh_mV"], marker= "D", color= "brown", s=80, zorder= 5, label= "Basement Sites")

# for i in dfdataNC.index:
#     if i in "Cr, Mo":
#         plt.annotate(i, xy= (dfdataNC.loc[i, "pH"], dfdataNC.loc[i, "Eh (mV)"]), 
#                  xytext= (1,-12), textcoords= "offset points", fontsize= 9)
# Literature data
# Literature
for country, color, label in [
    ("New Caledonia", "cornflowerblue", "NC (Literature)"),
    ("Oman", "grey", "Oman"),
    ("Philippines", "orange", "Philippines") #("Turkey", "lightcoral", "Turkey")
    ]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country to plot
    ax.scatter(
        dflitdata.loc[mask, "pH"],  # Filtered x-values
        dflitdata.loc[mask, "Eh (mV)"],      # Filtered y-values
        marker="o", s=35, color=color, label=label, zorder= 3)

# Zones
ax.plot((0,14), (0,-875), color= "darkslategray", linewidth=1.5)                     
c= 1200
ax.plot((0,14), (0+c,-875+c), color= "darkslategray", linewidth=1.5)

plt.annotate("O$_2$ STABLE", xy= (9, 900), xytext= (0, 0), textcoords= "offset points", fontsize= 13)
plt.annotate("Oxidizing", xy= (9, 750), xytext= (0, 0), textcoords= "offset points", fontsize= 13, alpha= 0.6)

plt.annotate("H$_2$O STABLE", xy= (1, 350), xytext= (0, 0), textcoords= "offset points", fontsize= 13)

plt.annotate("H$_2$ STABLE", xy= (5.5, -750), xytext= (0, 0), textcoords= "offset points", fontsize= 13)
plt.annotate("Reducing", xy= (5.5, -900), xytext= (0, 0), textcoords= "offset points", fontsize= 13, alpha= 0.6)          

# zone_ Surface water
ax.add_patch(Ellipse((8, 125), width= 2, height= 170, edgecolor= "black", facecolor='white', linestyle='--', lw=2))
plt.annotate("Surface water", xy= (6.5, 250), xytext= (0, 0), textcoords= "offset points", fontsize= 10)

# Mixture arrow
ax.add_patch(FancyArrowPatch((11, -750), (8, 125), 
                        connectionstyle="arc3,rad=0.4",  # Controls the curvature
                        arrowstyle="simple",  mutation_scale=60, color="gray", lw= 0, alpha= 0.4))
                                                         
ax.set_xlabel("pH", fontweight='bold', fontsize= 13) 
ax.set_ylabel("Eh (mV)", fontweight='bold', fontsize= 13)
ax.set_xlim(0, 14)
ax.set_ylim(-1100, 1100)
ax.legend(loc= "lower left", facecolor= "white")
# ax.set_xscale('log') 
# ax.set_yscale('log')

# Adding black border around figure
fig.patch.set_edgecolor('black')
fig.patch.set_linewidth(1.5)

plt.savefig('pH vs Eh.svg', format='svg', bbox_inches='tight')
