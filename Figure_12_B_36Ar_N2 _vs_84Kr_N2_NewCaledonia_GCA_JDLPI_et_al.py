# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:35:50 2025

@author: jdlpizerumug
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

dfdataNC = pd.read_excel(r"Compilation_rawdata_NC_2019_2020_2022.xlsx", sheet_name= "dataraw_ordered", index_col="IDss")
dflitdata= pd.read_excel(r"Literaturedata.xlsx", sheet_name="Serpent.Contexts", index_col="IDss")

# data by Type of sampled spring
Ophiolitic = dfdataNC[dfdataNC['Type'] == 'Ophiolitic']
Basement = dfdataNC[dfdataNC['Type'] == 'Basement']


# PLOTTING

# 36Ar vs 84Kr (Vacquand et al., 2018; Wang et al., 2022)
fig1, ax1 = plt.subplots()

ax1.scatter(Ophiolitic["36Ar"]/(Ophiolitic["N2"]/100), Ophiolitic["84Kr"]/(Ophiolitic["N2"]/100), marker= "D", color= "forestgreen", s=70, zorder= 3, label= "Ophiolitic (N.C)")
# ax1.scatter(Basement["36Ar"], Basement["84Kr"], marker= "D", color= "brown", s=70, zorder= 5, label= "Basement")


# ------------------------------------------------------------------------------------------------
# ENDMEMBERS (concentrations are in mol/mol)
# ------------------------------------------------------------------------------------------------

# Calculating endmembers following values in Vacquand et al., 2018 - tables 1&2
# Air endmembers
Ar36_air= 31.57e-06
Kr84_air= 0.65e-06
N2_air= 78.08e-02
Ar36_N2_air= Ar36_air / N2_air
Kr84_N2_air= Kr84_air / N2_air

# ASW endmembers
Ar36_asw= 1.07e-06
Kr84_asw= 0.04e-06
N2_asw= 1.23e-02 
Ar36_N2_asw= Ar36_asw / N2_asw
Kr84_N2_asw= Kr84_asw / N2_asw

"""
# Endmember verification
Ar_air= 0.934/100
f_Ar36_air= 0.00337         # Rosman & Taylor (1998, IUPAC)
Ar36_air= Ar_air * f_Ar36_air

Kr_air= 1.14/1000000
f_Kr84_air= 0.56987         # Rosman & Taylor (1998, IUPAC)
Kr84_air= Kr_air * f_Kr84_air

N2_air= 78.084/100

Ar36_N2_air= Ar36_air / N2_air
Kr84_N2_air= Kr84_air / N2_air

# ref of these previously used ASW endmembers?
Ar36_N2_asw= 0.000119                 
Kr84_N2_asw= 0.00000508
"""

# ------------------------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------------------------
ax1.scatter(Ar36_N2_air, Kr84_N2_air, marker= "*", color= "red", s=150, zorder= 4, label= "Endmembers") #Air
ax1.scatter(Ar36_N2_asw, Kr84_N2_asw, marker= "*", color= "red", s=100) #ASW


# Literature_ Plotting
# ax1.scatter(dflitdata["36Ar/N2"], dflitdata["84Kr/N2"], marker="o", s=35, color= "grey", label= "Ophiolites (literature)", zorder= 2)


for country, color, label in [
    ("New Caledonia", "cornflowerblue", "NC (Literature))"),
    ("Oman", "grey", "Oman"),
    ("Philippines", "orange", "Philippines"),
    ("Turkey", "lightcoral", "Turkey")]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country
    ax1.scatter(
        dflitdata.loc[mask, "36Ar/N2"],  # Filtered x-values
        dflitdata.loc[mask, "84Kr/N2"],      # Filtered y-values
        marker="o", s=35, color=color, label=label, zorder= 2)

ax1.set_xlabel("$\mathbf{^{36}Ar / N_2}$", fontweight='bold', fontsize=13)
ax1.set_ylabel("$\mathbf{^{84}Kr / N_2}$", fontweight='bold', fontsize=13)
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
ax1.annotate("Air", xy= (Ar36_N2_air, Kr84_N2_air), xytext= (-5, 10), textcoords= "offset points", fontsize= 10, fontweight= "bold")
ax1.annotate("ASW", xy= (Ar36_N2_asw, Kr84_N2_asw), xytext= (-10, 5), textcoords= "offset points", fontsize= 10, fontweight= "bold")

plt.annotate("B", xy=(1.4e-07, 8e-05), xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)

plt.legend(loc= 'lower right')

# saving the figure
plt.savefig('Figure_12_B_36Ar_N2_vs_84Kr_N2_NewCaledonia_GCA_JDLPI_et_al.svg', format='svg', bbox_inches='tight')
plt.savefig('Figure_12_B_36Ar_N2_vs_84Kr_N2_NewCaledonia_GCA_JDLPI_et_al.tiff', format='tiff', bbox_inches='tight')

plt.show()

