# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:37:41 2025

@author: jdlpizerumug
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import FancyArrowPatch


dfdataNC = pd.read_excel(r"Waterchemistry_Physicochempar.xlsx", sheet_name= "data_og", index_col="IDCs")
dflitdata= pd.read_excel(r"Literaturedata.xlsx", sheet_name="Serpent.Contexts_plot", index_col="IDss")

# plotting
fig, ax = plt.subplots()

# Grids
plt.grid(True, linestyle='--', linewidth=0.4)


# data
dfdataNC_South = dfdataNC[dfdataNC['Zone'] == 'South']
dfdataNC_North = dfdataNC[dfdataNC['Zone'] == 'North']

ax.scatter(dfdataNC_South.loc[:,"T (°C)"], dfdataNC_South.loc[:,"pH"], marker= "D", color= "forestgreen", s=80, zorder= 5, label= "Ophiolitic Sites")
ax.scatter(dfdataNC_North.loc[:,"T (°C)"], dfdataNC_North.loc[:,"pH"], marker= "D", color= "brown", s=80, zorder= 5, label= "Basement Sites")

"""
# PLOTTING EACH SITE WITH A SEPARATE SYMBOL
# Scatter points key
color_map = { 
    "La Crouen River":"brown",
    "Nemwegi": "brown",
    "Kopelia": "brown",
    "Gélima": "brown",
    "Mokoué River": "brown",
    "Fanama": "brown",
    "Pourina":"forestgreen",
    "Poco Mie": "forestgreen",
    "Lac Yaté": "forestgreen",
    "Bains des Japonais": "forestgreen", 
    "Bains des Kaoris": "forestgreen",
    "Lembi River": "forestgreen",
     }

marker_map = { 
    "La Crouen River":"P",
    "Nemwegi": "D",
    "Kopelia": ">",
    "Gélima": "^",
    "Mokoué River": "<",
    "Fanama": "s",
    "Pourina":"s",
    "Poco Mie": "v",
    "Lac Yaté": "^",
    "Bains des Japonais": "o", 
    "Bains des Kaoris": "X",
    "Lembi River": "d",
     }

# Fixed size for the data points
marker_size = 150

for site, group in dfdataNC.groupby("Site"):
    ax.scatter(
        group["T (°C)"], group["pH"],  # Ensure the order is [HCO3, OH, CO3_ right, top, left]
        marker=marker_map.get(site, "d"),
        color=color_map.get(site, "blue"),  
        label=site,
        s=marker_size,
        zorder=3)  # Set a high z-order to bring points in front
"""

# for i in dfdataNC.index:
#     if i in "Cr, Mo":
#         plt.annotate(i, xy= (dfdataNC.loc[i, "T (°C)"], dfdataNC.loc[i, "pH"]), 
#                  xytext= (1,-12), textcoords= "offset points", fontsize= 9)

#Literature data

# ax.scatter(dflitdata["T (°C)"], dflitdata["pH"], marker="o", s=35, color="grey", label= "ophiolites (Literature)", zorder= 3)


# Literature
for country, color, label in [
    ("New Caledonia", "cornflowerblue", "NC (Literature)"),
    ("Oman", "grey", "Oman"),
    ("UAE", "aqua", "UAE"),
    ("Japan", "darkorchid", "Japan"),
    ("Philippines", "orange", "Philippines")    # ("Turkey", "lightcoral", "Turkey")
    ]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country to plot
    ax.scatter(
        dflitdata.loc[mask, "T (°C)"],  # Filtered x-values
        dflitdata.loc[mask, "pH"],      # Filtered y-values
        marker="o", s=35, color=color, label=label, zorder= 3)


# Surface water
ax.add_patch(Ellipse((21, 7.75), width= 6, height= 3.6, edgecolor= "black", facecolor='white', linestyle='--', lw=2))
plt.annotate("Surface", xy= (18, 8), xytext= (-37, 20), textcoords= "offset points", fontsize= 10)
plt.annotate("water", xy= (19, 7.4), xytext= (-37, 20), textcoords= "offset points", fontsize= 10) 

"""
# Mixture arrow
ax.add_patch(FancyArrowPatch((42, 10), (21, 8), 
                        connectionstyle="arc3,rad=0.3",  # Controls the curvature
                        arrowstyle="simple",  mutation_scale=60, color="gray", lw= 0, alpha= 0.4))
"""

ax.set_xlabel("T (°C)", fontweight='bold', fontsize= 13) 
ax.set_ylabel("pH", fontweight='bold', fontsize= 13)
ax.set_xlim(10, 55)                         # set lowerlimit to 19 to zoom
ax.set_ylim(6, 14)
ax.legend(loc= "upper right", facecolor= "white", ncol= 3, 
          handletextpad= 0.001, columnspacing=0.3, borderpad=0.1)
# ax.set_xscale('log') 
# ax.set_yscale('log')

# Adding black border around figure
# fig.patch.set_edgecolor('black')
# fig.patch.set_linewidth(1.5)

plt.annotate("B", xy=(11.3, 13.95), xytext=(0, 0), ha='center', va='top', 
             textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)
plt.savefig('Figure_3_B_T_vs_pH_ NewCaledonia_GCA_JDLP_et_al.svg', format='svg', bbox_inches='tight')
plt.savefig('Figure_3_B_T_vs_pH_ NewCaledonia_GCA_JDLP_et_al.tiff', format='tiff', bbox_inches='tight')