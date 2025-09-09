# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 22:40:14 2025

@author: jdlpizerumug
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as pltp

dfdataNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                         sheet_name= "dataraw_ordered", index_col="IDss") 

dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx", sheet_name="Serpent.Contexts_plot", 
                         index_col="IDss")
dfliteraturedata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\Literaturedata_landserpentinisation.xlsx", 
                                index_col= "Country")   
#PLOTTING
fig, ax1 = plt.subplots()

# PLOTTING 
#plotting_this study
thisstudy= ax1.scatter(dfdataNC["dD_H2"], dfdataNC["dD_CH4"], marker= "D", s=50, color= "blue", label= "Ophiolitic" , zorder= 5)

#Plotting_ax1_Literature
for country, color, label, alpha in [
    # ("New Caledonia", "cornflowerblue", "NC (Literature)", 1),
    ("Oman", "grey", "Oman", 1),
    ("UAE", "aqua", "UAE", 0.8),
    ("Japan", "darkorchid", "Japan", 1),
    ("Philippines", "orange", "Philippines", 1),
    ("Turkey", "lightcoral", "Turkey", 1)]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country
    lit_scatter= ax1.scatter(
        dflitdata.loc[mask, "dD_H2"],        # Filtered x-values
        dflitdata.loc[mask, "dD_CH4"],      # Filtered y-values
        marker="o", s=35, color=color, label=label, alpha= alpha, zorder= 3)

ax1.set_zorder(1)            # Ensuring ax1 (scatter) is above ax2 (histogram)
ax1.patch.set_visible(False)  # Making ax1 background transparent so ax2 is not completely hidden

# Literature_data_compiled in Vacquand et al., (2018)
LostCity= ax1.add_patch(pltp.Ellipse((-650, -125), 100, 70, angle=0, linewidth=1, linestyle="--", edgecolor='none', facecolor='lightsteelblue', alpha= 0.8, zorder=0, label= "Lost City")) #VolcGasbig
HTOS= ax1.add_patch(pltp.Ellipse((-380, -110), 100, 50, angle=0, linewidth=1, linestyle="--", edgecolor='none', facecolor='steelblue', alpha= 0.7, zorder=0, label= "HTOS")) #VolcGasbig



#ax2_ plotting just Low Temperature Serp. data (excluding Larderello for instance)
ax2 = ax1.twinx()
binwidth= 10
dflit_LT= dfliteraturedata[dfliteraturedata["Temp"]=="LowTemp"]
n_lit_LT= dflit_LT["dD_H2"].count()  #Counting the number of data available

lit_hist= ax2.hist(dflit_LT.loc[:,"dD_H2"], color="limegreen", alpha= 0.2, lw=0, label= f"Land Serp. (n= {n_lit_LT})", zorder= 0,
         bins= np.arange(math.floor(dflit_LT["dD_H2"].min()/10)*10, math.ceil(dflit_LT["dD_H2"].max()/10)*10 + binwidth, binwidth))


        
# Legend
# Combining handles and labels from both axes
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# Plotting the combined legend
ax1.legend(handles1 + handles2, labels1 + labels2, loc='lower right')

# Setting axes limits
ax1.set_xlim(-800, -300)
ax1.set_ylim(-450, 0)
ax2.set_ylim(0, 7)


# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1)
    
# plt.title("δD_CH4 vs δ13C_CH4", fontweight= "bold")
ax1.set_xlabel("δD($\mathbf{H_2}$) (‰ VSMOW)", fontweight='bold', fontsize= 13)
ax1.set_ylabel("δD($\mathbf{CH_4}$) (‰ VSMOW)", fontweight='bold', fontsize= 13)
ax2.set_ylabel("Frequency (n)", fontweight='bold', fontsize= 13)

# ax1.set_legend(loc= "lower right", fontsize= 9.5, facecolor= "white")
# ax2.set_legend(loc= "lower right", fontsize= 9.5, facecolor= "white")

# for text in legend.get_texts():
#     text.set_color('white')

# Annotating figure number
ax1.annotate("B", xy=(-320, -10), xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)
                

plt.savefig('dD_H2vsdD_CH4_NewCaledonia.svg', format='svg', bbox_inches='tight')
plt.show()