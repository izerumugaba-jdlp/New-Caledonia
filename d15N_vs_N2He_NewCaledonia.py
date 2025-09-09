# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 03:22:17 2025

@author: jdlpizerumug
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Distinguishing the origins of N2 in N2-dominated gases

# Importing files
dfdataNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx", 
                         sheet_name="dataraw_ordered", index_col="IDss")

dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx", sheet_name="Serpent.Contexts", 
                         index_col="IDss")
dflitfischer= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Litdata_N2_Fischer2002.xlsx")

dfendmembers= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\python_phD\endmembers.xlsx")

# Fixed end-member values (Fischer et al., 2002)
d15N_air= 0
d15N_morb= -5
d15N_sed= 7

N2_He_air= 1.5e05
N2_He_morb= 150
N2_He_sed= 10500

# Concentrations of N2 in endmembers. # for N2-dominated gases in subduction zones, consider 90 mol% N2 i.e 0.9 mol/mol for MORB and recycled sediments.
N2_air= 0.78
N2_morb= 0.9
N2_sed= 0.9

# Calculating He from N2 and N2/He: He= N2 / (N2/He)
He_air= N2_air / N2_He_air
He_morb= N2_morb / N2_He_morb
He_sed= N2_sed / N2_He_sed

# Mixing fractions, given f
f = np.linspace(0, 1, 100000)

# Mixing between Air and MORB
N2_air_morb= (N2_air * f) + (N2_morb * (1-f))
He_air_morb= (He_air * f) + (He_morb * (1-f))
N2_He_air_morb= N2_air_morb / He_air_morb

d15N_air_morb= (d15N_air * f)+ (d15N_morb * (1-f))

# Mixing between Air and sed
N2_air_sed= (N2_air * f) + (N2_sed * (1-f))
He_air_sed= (He_air * f) + (He_sed * (1-f))
N2_He_air_sed= N2_air_sed / He_air_sed

d15N_air_sed= (d15N_air * f) + (d15N_sed * (1-f))

# Mixing between MORB and sed
N2_morb_sed= (N2_morb * f) + (N2_sed * (1-f))
He_morb_sed= (He_morb * f) + (He_sed * (1-f))
N2_He_morb_sed= N2_morb_sed / He_morb_sed

d15N_morb_sed= (d15N_morb * f) + (d15N_sed * (1-f))
#----------------------------------------------------------------------------------------------------------------------------------------------------


# PLOTTING
fig, ax = plt.subplots()


# Plotting Endmembers
dfendmembers_f= dfendmembers.drop([2, 11])           #dropping indices whose data i dont wanna show on the plot
Endmembers= plt.plot(dfendmembers_f.loc[:,"d15N_m"],dfendmembers_f.loc[:,"N2/He"], "r*", ms=13, label= "Endmembers", zorder= 3)

# Mixing curves between endmembers
plt.plot(d15N_air_morb, N2_He_air_morb, "k--", linewidth= 1)
plt.plot(d15N_air_sed, N2_He_air_sed, "k--", linewidth= 1)
plt.plot(d15N_morb_sed, N2_He_morb_sed, "k", linewidth= 1.5)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Mixing between air and different proportions MORB-sed (ms) mixtures
f_m_ms= [i/100 for i in [30, 5]]              #fraction of MORB mantle

He_ms= [(j * He_morb) + ((1 - j) * He_sed) for j in f_m_ms]
N2_ms= [(j * N2_morb) + ((1 - j) * N2_sed) for j in f_m_ms]
d15N_ms= [(j * d15N_morb) + ((1 - j) * d15N_sed) for j in f_m_ms]

for N2_ms_1, He_ms_1, d15N_ms_1 in zip(N2_ms, He_ms, d15N_ms):
    
    # Getting the concentrations of He in ms
    N2_He_ms= N2_ms_1 / He_ms_1

    # Performing mixing air-ms i.e calculating N2, He, N2/He and d15N values at each step of the mixture
    N2_mix_a_ms = (f * N2_air) + ((1 - f) * N2_ms_1)
    He_mix_a_ms = (f * He_air) + ((1 - f) * He_ms_1)
    N2_He_mix_a_ms= N2_mix_a_ms / He_mix_a_ms
    d15N_mix_a_ms = (f * d15N_air) + ((1 - f) * d15N_ms_1)
    
    # Plotting mixing curves
    plt.plot(d15N_mix_a_ms, N2_He_mix_a_ms, "k--", linewidth= 1)

# Annotating 70% , 95% Sed and contributions to the mantle mixture
ax.annotate ("95%", xy=(6.6, 1.8e03), xytext=(0,0), textcoords='offset points')
ax.annotate ("70%", xy=(3.3, 2.8e02), xytext=(0,0), textcoords='offset points')
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Plotting datapoints
ophiolitic = dfdataNC[dfdataNC["Type"] == "Ophiolitic"]
basement = dfdataNC[dfdataNC["Type"] == "Basement"]
ax.scatter(ophiolitic["d15N_m"],((ophiolitic["N2"]/100)/(ophiolitic["4He"]+ophiolitic["3He"])), marker= "D", s=45, color= "forestgreen", label= "Ophiolitic", zorder= 5)
ax.scatter(basement["d15N_m"],((basement["N2"]/100)/(basement["4He"]+basement["3He"])), marker= "D", s=45, color= "brown", label= "Basement", zorder= 5)

# Plotting literature data Fischer et al., 2022
for country, marker, edgecolor, label1 in [
    ("Guatemala", "o", "black", "Guatemala"),
    ("Costa Rica", "^", "black", "Costa Rica")]:
    
    mask = dflitfischer["Country"] == country  # Filtering data for the current country
    ax.scatter(
        dflitfischer.loc[mask, "d15N"],        # Filtered x-values
        dflitfischer.loc[mask,"N2/He"],      # Filtered y-values
        s=35, edgecolors=edgecolor, facecolors= "none", marker=marker, label=label1, zorder= 1)

# Plotting literature data_ serpentinisation contexts
for country, color, label2 in [
    ("New Caledonia", "cornflowerblue", None),
    ("Oman", "grey", "Oman"),
    ("Philippines", "orange", "Philippines"),
    ("Turkey", "lightcoral", None)]:
    
    mask = dflitdata["Country"] == country  # Filtering data for the current country
    ax.scatter(
        dflitdata.loc[mask, "d_15N"],        # Filtered x-values
        (dflitdata.loc[mask,"N2"]/100)/(dflitdata.loc[mask,"4He"]+dflitdata.loc[mask,"3He"]),      # Filtered y-values
        marker="o", s=35, color=color, label=label2, zorder= 4)

plt.xlim(-6, 8)
plt.ylim(10**1, 10**6)
plt.legend(loc= "upper left", fontsize= 9)
# plt.xscale("log")
plt.yscale("log")   #varry log to linear scale for y to see changes
plt.xlabel("$\mathbf{δ^{15}N}$", fontweight='bold', fontsize= 13) 
plt.ylabel("$\mathbf{N_2}$/He", fontweight='bold', fontsize= 13)

# Annotation of endmembers
for i in dfendmembers.index:
    if i==0 or i==9:
        ax.annotate((dfendmembers.loc[i,"Label"]), xy=(dfendmembers.loc[i,"d15N_m"], dfendmembers.loc[i,"N2/He"]), 
                        fontsize= 11, xytext=(-7, 7), textcoords='offset points')
    if i==3:
        ax.annotate((dfendmembers.loc[i,"Label"]), xy=(dfendmembers.loc[i,"d15N_m"], dfendmembers.loc[i,"N2/He"]), 
                        fontsize= 11, xytext=(-10, -15), textcoords='offset points')
    
    else:
        continue
    
# Annotating data points
for i in dfdataNC.index:
    if i==2 or i==9:
        ax.annotate(dfdataNC.loc[i,"IDs"], xy=(dfdataNC.loc[i,"d15N_m"], dfdataNC.loc[i,"N2/He"]), 
                        fontsize= 11, xytext=(5,-5), textcoords='offset points')
    elif i==8:
        ax.annotate(dfdataNC.loc[i,"IDs"], xy=(dfdataNC.loc[i,"d15N_m"], dfdataNC.loc[i,"N2/He"]), 
                        fontsize= 11, xytext=(5,0), textcoords='offset points') 
                
# Annotating figure number
plt.annotate("A", xy=(7.5, 7e05), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)


plt.savefig("d15N_vs_N2He_NewCaledonia.svg", format= "svg", bbox_inches='tight')
plt.show()





























