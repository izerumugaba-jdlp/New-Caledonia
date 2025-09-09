# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:10:11 2024

@author: jdlpizerumug
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Importing data
dfdataNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                         sheet_name= "dataraw_ordered", index_col="IDss")
dfendmembers = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\python_phD\endmembers.xlsx", index_col=("Environment"))

# data by Zones of sampling
dfdataNC_Ophiolitic = dfdataNC[dfdataNC['Type'] == 'Ophiolitic']
dfdataNC_Basement = dfdataNC[dfdataNC['Type'] == 'Basement']

# PLOTTING
fig, ax = plt.subplots()

# Plotting 
norm_colorscale = mcolors.Normalize(vmin= -100, vmax= 0)  #Normalizing the color bar scale
dataOphiolitic= ax.scatter(dfdataNC_Ophiolitic["CH4"], dfdataNC_Ophiolitic["H2"], c= dfdataNC_Ophiolitic["d13C_CH4"], cmap="Greens", norm= norm_colorscale, marker= "o", s=100, label="Ophiolitic") # c=z applies color mapping
dataBasement= ax.scatter(dfdataNC_Basement["CH4"], dfdataNC_Basement["H2"], c= dfdataNC_Basement["d13C_CH4"], cmap="Oranges", norm= norm_colorscale, marker= "o", s=100, label="Basement") # c=z applies color mapping

# Adding color bars with bold label
cbar1 = plt.colorbar(dataOphiolitic)
cbar1.set_label("δ13C $\mathbf{CH_4}$ (‰ VPDB)", fontweight='bold', fontsize=11)
cbar2= plt.colorbar(dataBasement)

# Adjusting plot
cbar2.set_ticks([])      #removing the ticks and ticklabels
# Adjusting position of cbar2 relative to cbar1
pos1 = cbar1.ax.get_position()
cbar2.ax.set_position([pos1.x0 - 0.032, pos1.y0, pos1.width, pos1.height])
# Adjusting the size of the main plot
pos = ax.get_position()  # Get current position
ax.set_position([pos.x0, pos.y0, pos.width * 1.25, pos.height])  # Increasing the plt's plot width -12, 5


# Annotating
for i in dfdataNC.index:
    if i in ["BK1", "BK21", "BK23", "BJ2", "BJ1", "L2B", "BK2", "Prg", "L2", "L1B", "Prn2", "Cr"]:
        plt.annotate(i, xy= (dfdataNC.loc[i, "CH4"], dfdataNC.loc[i, "H2"]), xytext= (4, -1), textcoords= "offset points", fontsize= 10)
    elif i in ["TS2"]:
        plt.annotate("T", xy= (dfdataNC.loc[i, "CH4"], dfdataNC.loc[i, "H2"]), xytext= (2, -14), textcoords= "offset points", fontsize= 10)
    
    elif i in ["Mo2"]:
        plt.annotate(i, xy= (dfdataNC.loc[i, "CH4"], dfdataNC.loc[i, "H2"]), xytext= (-11, 7), textcoords= "offset points", fontsize= 10)
    elif i in ["Fnm"]:
        plt.annotate(i, xy= (dfdataNC.loc[i, "CH4"], dfdataNC.loc[i, "H2"]), xytext= (-5, 9), textcoords= "offset points", fontsize= 10, rotation=30)
    elif i in ["Nmg1"]:
        plt.annotate(i, xy= (dfdataNC.loc[i, "CH4"], dfdataNC.loc[i, "H2"]), xytext= (-1, 7), textcoords= "offset points", fontsize= 10, rotation=30)
    elif i in ["L1", "LA", "Co", "PM1", "Co1B", "Prn1"]:
        plt.annotate(i, xy= (dfdataNC.loc[i, "CH4"], dfdataNC.loc[i, "H2"]), xytext= (-4, -12), textcoords= "offset points", fontsize= 10)
        
        


# Computing the line of best fit (linear regression correlation, which essentially minimizes the distance btn datapoints and the line, 
# using the least squares regression. (squares because the distance in units of the plot can be negative))
# This line of best fit is for samples rich in H2
H2_richdata= dfdataNC[dfdataNC["H2"] >= 5][dfdataNC["CH4"] >= 5] # data where H2 and CH4 > 5%
# Computing the line
slope, intercept = np.polyfit(H2_richdata["CH4"], H2_richdata["H2"], 1)
x_vals = np.array([H2_richdata["CH4"].min() -1 , H2_richdata["CH4"].max() + 3])
y_vals_bf = intercept + (slope * x_vals)

# Getting the correlation coefficient (R) between CH4 and H2
R_matrix = np.corrcoef (H2_richdata["CH4"], H2_richdata["H2"])
R= R_matrix[1, 0]

# Visualizing the slope and intercept
print("Slope:", slope)
print("Intercept:", intercept)
print("R= ", R)

# Methane generation processes lines (Monnin et al., 2021 p. 11)
y_vals_sabatier= -0.25 * x_vals + 20
y_vals_FTT= -0.33 * x_vals + 20
y_vals_elt_C= -0.5 * x_vals + 20

# Plotting the lines
linebf, = ax.plot(x_vals, y_vals_bf, color="gray", linestyle="--") #, label="Best Fit ([H2] and [CH4] > 5%); R=-0.6"



plt.xlabel(r"[$\mathbf{CH_4}$] (mol %)", fontweight= "bold", fontsize=13)
plt.ylabel(r"[$\mathbf{H_2}$] (mol %)", fontweight= "bold", fontsize=13)
plt.xlim(-3, 28)
plt.ylim(-3, 38)      # 0.01, 100
# plt.yscale("log")


# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1)

# handlesdata= [datapoints, linebf]
plt.legend(loc= "upper right", fontsize= 10)
plt.savefig("CH4vsH2_ NewCaledonia.svg", format= "svg", bbox_inches='tight')

plt.show()