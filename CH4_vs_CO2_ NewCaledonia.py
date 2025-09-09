# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 17:55:17 2025

@author: jdlpizerumug
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

dfdataNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                         sheet_name= "dataraw_ordered", index_col="IDss")

# data by Zones of sampling
dfdataNC_Ophiolitic = dfdataNC[dfdataNC['Type'] == 'Ophiolitic']
dfdataNC_Basement = dfdataNC[dfdataNC['Type'] == 'Basement']

# PLOTTING
fig, ax = plt.subplots()

# Plotting 
norm_colorscale = mcolors.Normalize(vmin= -100, vmax= 0)  #Normalizing the color bar scale
dataOphiolitic= ax.scatter(dfdataNC_Ophiolitic["CH4"], dfdataNC_Ophiolitic["CO2"], c= dfdataNC_Ophiolitic["d13C_CH4"], cmap="Greens", norm= norm_colorscale, marker= "o", s=100, label="Ophiolitic") # c=z applies color mapping
dataBasement= ax.scatter(dfdataNC_Basement["CH4"], dfdataNC_Basement["CO2"], c= dfdataNC_Basement["d13C_CH4"], cmap="Oranges", norm= norm_colorscale, marker= "o", s=100, label="Basement") # c=z applies color mapping

# Adding color bars with bold label
cbar1 = plt.colorbar(dataOphiolitic)
cbar1.set_label("δ$\mathbf{^{13}C(CH_4)}$ (‰ VPDB)", fontweight='bold', fontsize= 13)
cbar2= plt.colorbar(dataBasement)

# Adjusting plot
cbar2.set_ticks([])      #removing the ticks and ticklabels
# Adjusting position of cbar2 relative to cbar1
pos1 = cbar1.ax.get_position()
cbar2.ax.set_position([pos1.x0 - 0.032, pos1.y0, pos1.width, pos1.height])
# Adjusting the size of the main plot
pos = ax.get_position()  # Get current position
ax.set_position([pos.x0, pos.y0, pos.width * 1.25, pos.height])  # Increasing the plt's plot width

plt.xlabel(r"[$\mathbf{CH_4}$] (mol %)", fontweight='bold', fontsize= 13)
plt.ylabel(r"[$\mathbf{CO_2}$] (mol %)", fontweight='bold', fontsize= 13)
plt.xlim(-3, 23)
plt.ylim(0.01, 1.5)
plt.yscale("log")

# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1)
    
plt.legend(loc= "upper right", fontsize=11)

# Annotating figure number
plt.annotate("A", xy=(-1.8, 1.4), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)

# plt.legend(handles= handlesdata, fontsize= 8.5)
plt.savefig("CH4vsCO2_ NewCaledonia.svg", format= "svg", bbox_inches='tight')

plt.show()