# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:42:35 2024

@author: jdlpizerumug
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as pltp


dfdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Python_Nouvelle Caledonie\Test_Hisotopefractionation.xlsx", 
                      index_col=("Samples"))

R_D_H_SMOW= 0.00015576     # Standard D/H (Hagemann et al. (1970); (Tse et al. (1980); De Wit et al. (1980)))

# Isotopic ratios (deuterium/ protium)
dfdata["R_D_H_CH4"]= ((dfdata["dD_CH4"] / 1000) + 1) * R_D_H_SMOW
dfdata["R_D_H_H2"]= ((dfdata["dD_H2"] / 1000) + 1) * R_D_H_SMOW
dfdata["R_D_H_H2O"]= ((dfdata["dD_H2O"] / 1000) + 1) * R_D_H_SMOW


# FRACTIONATION FACTORS_ ALPHA
dfdata["alpha_CH4_H2"]= dfdata["R_D_H_CH4"] / dfdata["R_D_H_H2"]
dfdata["alpha_H2O_H2"]= dfdata["R_D_H_H2O"] / dfdata["R_D_H_H2"]
dfdata["alpha_CH4_H2O"]= dfdata["R_D_H_CH4"] / dfdata["R_D_H_H2O"]
dfdata["alpha_H2_H2O"]= dfdata["R_D_H_H2"] / dfdata["R_D_H_H2O"]

# Isotopic Equilibrium Line data_ alpha_CH4_H2
# The D_H fractionation factor btn CH4 and H2 at equilibrium fits the equation alpha= 0.8994 + (183540 / (T**2)) between T= 200 - 500 celcius degrees (Horibe and Graig, 1995)
# Temperature values (0 - 500°C)
T_C= np.arange(0, 501, 50)
T= np.arange((0+273.15), (501+273.15), (50))                 # T in the equation are in K, hence the adjustement
alph_eq_CH4_H2= 0.8994 + (183540 / (T**2))

# Isotopic Equilibrium Line data_ alpha_H2O(l)_H2
# The D_H fraction in this case follows the equation, recalibrated from previous measurements between 0 and 370°C (Horibe and Graig, 1995): 
alpha_eq_H2Ol_H2= 1.0473 + (201036/(T**2)) + (2.060 * (10**9/(T**4))) + (0.180 * (10**15 / (T**6)))

# dataframe of equilibrium parameters
df_eq_param= pd.DataFrame({"T_C": T_C, 
                           "T_K": T , "alph_eq_CH4_H2": alph_eq_CH4_H2, 
                           "alpha_eq_H2Ol_H2":alpha_eq_H2Ol_H2},
                          index= T_C)

# PLOTTING_ alpha
fig1, ax = plt.subplots()
# datapoints by site
for site, marker, markersize, color, label, zorder in [
        ("NC", "D", 70, "forestgreen", "Ophiolitic (N.C)", 2),
        ("Larderello", "o", 50, "black", "Larderello", 1),
        ("Oman", "o", 50, "grey", "Oman", 1),
        ("UAE", "o", 50, "aqua", "UAE", 1),
        ("Japan", "o", 50, "darkorchid", "Hakuba Happo", 1),
        ("Philippines", "o", 50, "orange", "Philippines", 3),
        ("Turkey", "o", 50, "lightcoral", "Turkey", 3)]:
    df_site= dfdata[dfdata["Site"] == site]
    plt.scatter(df_site["alpha_H2O_H2"], df_site["alpha_CH4_H2"], marker= marker, s=markersize, color= color, label= label, zorder= zorder)
        
# Eq line
plt.scatter(alpha_eq_H2Ol_H2, alph_eq_CH4_H2, marker= "_", color= "black", s= 500)
plt.plot(alpha_eq_H2Ol_H2, alph_eq_CH4_H2, linestyle= "-", color= "black", label= "Eq. Line")

for i in df_eq_param.index:
    if i in [0, 50, 100, 150, 200, 250, 300, 400, 500]:
        plt.annotate(df_eq_param.loc[i, "T_C"], xy=(df_eq_param.loc[i, "alpha_eq_H2Ol_H2"], df_eq_param.loc[i, "alph_eq_CH4_H2"]), 
                 xytext=(12,-3), textcoords='offset points', fontsize=8)

# Other Literature data (compiled in Leila et al., 2021)
ax.add_patch(pltp.Ellipse((-510, -390), 16, 37, angle=55, edgecolor='k', facecolor='none', linewidth=1, linestyle="--"))


# Plot formatting
plt.xlabel("α($\mathbf{H_2O-H_2}$)", fontweight='bold', fontsize= 14)
plt.ylabel("α($\mathbf{CH_4-H_2}$)", fontweight='bold', fontsize= 14)
plt.xlim(1, 5)
plt.ylim(1, 3.5)
plt.xticks(rotation= 0, fontsize= 11)
plt.yticks(rotation= 0, fontsize= 11)

# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1.5)
    
plt.legend(fontsize= 9, loc= "lower right")

# Annotating figure number
plt.annotate("A", xy=(1.15, 3.45), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)

plt.savefig('H_isotopes_fract_alpha_NewCaledonia.svg', format='svg', bbox_inches='tight')
plt.show()


#%%

# FRACTIONATION FACTORS_EPSILON
dfdata["epsilon_CH4_H2"]= 1000 * (np.log(dfdata["alpha_CH4_H2"]))
dfdata["epsilon_CH4_H2"]= 1000 * (np.log(dfdata["alpha_CH4_H2"]))
dfdata["epsilon_CH4_H2O"]= 1000 * (np.log(dfdata["alpha_CH4_H2O"]))
dfdata["epsilon_H2_H2O"]= 1000 * (np.log(dfdata["alpha_H2_H2O"]))

# Equilibrium line epsilon
# The plot will be epsilon-H2-H2O vs epsilon-CH4-H2O. let's calculate these parameters
alpha_eq_H2_H2Ol= 1/alpha_eq_H2Ol_H2
epsilon_eq_H2_H2Ol= 1000 * (np.log(alpha_eq_H2_H2Ol))
alpha_eq_H2Ol_CH4= 1.0997 + (8456/(T**2)) + (0.9611*(10**9/(T**4))) - (27.82*(10**12/(T**6)))  #(range 0-370°C; but low sensitivity btn 250 and 350 Horibe and Craig.; 1995)
alpha_eq_CH4_H2Ol= 1/alpha_eq_H2Ol_CH4
epsilon_eq_CH4_H2Ol= 1000 * (np.log(alpha_eq_CH4_H2Ol))


# saving the calculated eq.line data to dataframe
dfeqeps= pd.DataFrame({"alpha_eq_H2_H2Ol": alpha_eq_H2_H2Ol, 
                       "epsilon_eq_H2_H2Ol": epsilon_eq_H2_H2Ol,
                       "alpha_eq_H2Ol_CH4": alpha_eq_H2Ol_CH4,
                       "alpha_eq_CH4_H2Ol": alpha_eq_CH4_H2Ol,
                       "epsilon_eq_CH4_H2Ol": epsilon_eq_CH4_H2Ol},
                      index= T_C)

df_eq_params= pd.concat([df_eq_param, dfeqeps], axis=1)

# PLOTTING_epsilon
fig2, ax = plt.subplots()
# datapoints by site
handles_pts = []  # collecting handles for data points and Eqline here
for site, marker, markersize, color, label, zorder in [
        ("Larderello", "o", 50, "black", "Larderello", 3),
        ("Oman", "o", 50, "grey", "Oman", 3),
        ("UAE", "o", 50, "aqua", "UAE", 1),
        ("Japan", "o", 50, "darkorchid", "Hakuba Happo", 3),
        ("Philippines", "o", 50, "orange", "Philippines", 3),
        ("Turkey", "o", 50, "lightcoral", "Turkey", 3),
        ("NC", "D", 70, "forestgreen", "Ophiolitic (NC)", 4)]:
    df_site= dfdata[dfdata["Site"] == site]
    datapoints= plt.scatter(df_site["epsilon_H2_H2O"], df_site["epsilon_CH4_H2O"], marker= marker, s= markersize, color= color, label= label)
    handles_pts.append(datapoints)

# Eq line
plt.scatter(epsilon_eq_H2_H2Ol, epsilon_eq_CH4_H2Ol, marker= "|", color= "black", s= 200)
eqline, = plt.plot(epsilon_eq_H2_H2Ol, epsilon_eq_CH4_H2Ol, linestyle= "-", color= "black", label= "Eq. Line")
handles_pts.append(eqline)

for i in df_eq_params.index:
    if i in [0, 50, 100, 150, 200, 250, 300, 400, 500]:
        plt.annotate(df_eq_params.loc[i, "T_C"], xy=(df_eq_params.loc[i, "epsilon_eq_H2_H2Ol"], df_eq_params.loc[i, "epsilon_eq_CH4_H2Ol"]), 
                 xytext=(-7,-18), textcoords='offset points', fontsize=8)

# Literature data (compiled in Leila et al., 2021)
volcgas= ax.add_patch(pltp.Ellipse((-510, -390), 400, 150, angle=30, linewidth=1, linestyle="--", edgecolor='none', facecolor='lightsteelblue', alpha= 0.8, zorder=0, label= "Volcanic gas")) #VolcGasbig
ax.add_patch(pltp.Ellipse((-795, -80), 140, 100, angle=90, linewidth=1, linestyle="--", edgecolor='none', facecolor='lightsteelblue', alpha= 0.8, zorder=0)) #VolcGassml
lostcity= ax.add_patch(pltp.Ellipse((-1050, -110), 300, 120, angle=0, linewidth=1, linestyle="--", edgecolor='none', facecolor='darkkhaki', alpha= 0.5, zorder=0, label= "Lost City")) #lostCity
htos= ax.add_patch(pltp.Ellipse((-480, -110), 250, 120, angle=0, linewidth=1, linestyle="--", edgecolor='none', facecolor='steelblue', alpha= 0.7, zorder=0, label="HTOS")) #HightempOcSet


# Plot formatting
plt.xlabel("ε($\mathbf{H_2-H_2O}$)‰", fontweight='bold', fontsize= 14)
plt.ylabel("ε($\mathbf{CH_4-H_2O}$)‰", fontweight='bold', fontsize= 14)
# plt.xlim(-1600, 0)
# plt.ylim(-900, 0)
plt.xticks(rotation= 0, fontsize= 11)
plt.yticks(rotation= 0, fontsize= 11)

# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1.5)
    
# Legend 1
# legend1= ax.legend(handles= handles_pts, loc= "lower left")
# ax.add_artist(legend1)  # Adding the first legend manually, otherwise it would have been replaced by legend 2

# extracting handles for legend 2
handles_lit= [volcgas, lostcity, htos]
# Legend 2
legend2= ax.legend(handles= handles_lit, loc= "lower right")

# Annotating figure number
plt.annotate("B", xy=(-1530, 0), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)

plt.savefig('H_isotopes_fract_epsilon_NewCaledonia.svg', format='svg', bbox_inches='tight')
plt.show()