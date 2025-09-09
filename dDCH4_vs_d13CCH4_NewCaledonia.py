# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:56:39 2023

@author: jdlpizerumug
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as pltp

dfdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Python_Nouvelle Caledonie\Test_Hisotopefractionation.xlsx", 
                             sheet_name= "ThisStudy_NC", index_col= "IDs")

dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx", sheet_name="Serpent.Contexts_plot", 
                         index_col="IDss")
# dflitdata= pd.to_numeric(dflitdata)
#Methane genesis fields (Milkov and Etiope.; 2018)
#Abiotic
Xab= [-450, -300, -50, -50, -350, -450, -450]
Yab= [-50, -50, -20, +10, +10, -10, -50]

#Fermentation (F)
Xf= [-450, -450, -250, -250, -450]
Yf= [-50, -90, -90, -50, -50]

#CO2-Reduction (CR)- originated
Xcr= [-350, -350, -100, -100, -350]
Ycr= [-60, -90, -90, -60, -60]

#Thermogenic
Xtg= [-350, -350, -100, -150, -300, -350]
Ytg= [-60, -75, -40, -15, -40, -60]

#Secondary Microbial (SM)
Xsm= [-350, -180, -150, -190, -350]
Ysm= [-60, -60, -35, -35, -60]

#Land Serpentinization
Xls= [-200, -200, -260, -235, -270, -85, -86, -350, -338, -310, -200]
Yls= [-35, -34, -32, -28.2, -16.2, -12.9, -3.1, -11, -36.5, -38.1, -35]

#Volcanic Geothermal
Xvg=[-140, -60, -85, -113, -138, -201, -251, -189, -140]
Yvg= [-27.8, -20.2, -12.9, -8.5, -8.9, -13.8, -23.9, -27.5, -27.8]


#PLOTTING
fig, ax = plt.subplots()
#Fields
ax.plot(Xab, Yab, color="purple", linewidth=1)
ax.plot(Xf, Yf, color="cornflowerblue", linewidth=1)
ax.plot(Xcr, Ycr, color="royalblue", linewidth=1)
ax.plot(Xtg, Ytg, color="red", linewidth=1)
ax.plot(Xsm, Ysm, color="black", linestyle= "--", linewidth=1)
ax.plot(Xls, Yls, color="lightgreen", linestyle= ":", linewidth=2)
ax.plot(Xvg, Yvg, color="deeppink", linestyle= "--", linewidth=1.5)

#Fields fill
plt.fill(Xab, Yab, color= "purple", alpha= 0.1)
plt.fill(Xf, Yf, color= "cornflowerblue", alpha= 0.1)
plt.fill(Xcr, Ycr, color= "royalblue", alpha= 0.1)
plt.fill(Xtg, Ytg, color= "red", alpha= 0.1)
plt.fill(Xsm, Ysm, color= "black", alpha= 0.2)
plt.fill(Xls, Yls, color= "green", alpha= 0.2)
plt.fill(Xvg, Yvg, color= "deeppink", alpha= 0.1)


#Fields Annotations
ax.annotate("Abiotic", xy=(-420, -30), xytext=(-420, -30), size= 15, color="purple")
ax.annotate("F", xy=(-400, -60), xytext=(-400, -60), size= 15, color="cornflowerblue")
ax.annotate("CR", xy=(-200, -70), xytext=(-200, -70), size= 15, color="royalblue")
ax.annotate("Primary microbial", xy=(-390, -80), xytext=(-390, -80), size= 15, color="royalblue")
ax.annotate("Thermogenic", xy=(-150, -40), xytext=(-150, -40), size= 13, color="red", rotation= 5)
ax.annotate("EMT", xy=(-348, -62), xytext=(-348, -62), size= 15, color="red")
ax.annotate("OA", xy=(-195, -40), xytext=(-195, -40), size= 15, color="red")
ax.annotate("LMT", xy=(-165, -28), xytext=(-165, -30), size= 15, color="red", alpha= 1)
ax.annotate("SM", xy=(-225, -50), xytext=(-225, -50), size= 15, color="black")
ax.annotate("Land Serp.", xy=(-270, -11), xytext=(-270, -11), size= 13, color="darkgreen", zorder= 5)

ax.annotate("Volcanic &", xy=(-90, -32), xytext= (0, 0), textcoords='offset points', size= 11, color="deeppink"
            , alpha= 0.7, rotation= 10)
ax.annotate("geothermal", xy=(-90, -27), xytext= (0, 0), textcoords='offset points', size= 11, color="deeppink",
             alpha= 0.7, rotation= 10)
ax.add_patch(pltp.FancyArrow(-67, -27, -30, 10, width=0.4, color='deeppink', length_includes_head=True))

# PLOTTING by site_ this study

for Type, marker, color, label, zorder in [
        ("Ophiolitic", "D", "blue", "Ophiolitic", 5),
        ("Basement", "D", "maroon", "Basement", 6)]:
    df_Type= dfdata[dfdata["Type"] == Type]
    plt.scatter(df_Type["dD_CH4"], df_Type["d13C_CH4"], marker= marker, s=50, color= color, label= label, zorder= zorder)
    for i in df_Type.index:
        if i in ["Nmg1", "Fnm"]:
            ax.annotate(df_Type.loc[i, "IDCs"], xy=(df_Type.loc[i, "dD_CH4"], df_Type.loc[i, "d13C_CH4"]), xytext=(-3,6), textcoords='offset points', fontsize=12)
        elif i in ["BK23", "Prg"]:
            ax.annotate(df_Type.loc[i, "IDCs"], xy=(df_Type.loc[i, "dD_CH4"], df_Type.loc[i, "d13C_CH4"]), xytext=(2,4), textcoords='offset points', fontsize=12)
        elif i in ["PM1"]:
            ax.annotate(df_Type.loc[i, "IDCs"], xy=(df_Type.loc[i, "dD_CH4"], df_Type.loc[i, "d13C_CH4"]), xytext=(-15,5), textcoords='offset points', fontsize=12)
        elif i in ["Co1C"]:
            ax.annotate(df_Type.loc[i, "IDCs"], xy=(df_Type.loc[i, "dD_CH4"], df_Type.loc[i, "d13C_CH4"]), xytext=(2,-10), textcoords='offset points', fontsize=12)
        elif i in ["Prn2"]:
            ax.annotate(df_Type.loc[i, "IDCs"], xy=(df_Type.loc[i, "dD_CH4"], df_Type.loc[i, "d13C_CH4"]), xytext=(6,-8), textcoords='offset points', fontsize=12)
        elif i in ["L2B"]:
            ax.annotate(df_Type.loc[i, "IDCs"], xy=(df_Type.loc[i, "dD_CH4"], df_Type.loc[i, "d13C_CH4"]), xytext=(-13,-10), textcoords='offset points', fontsize=12)
        elif i in ["LA"]:
            ax.annotate(df_Type.loc[i, "IDCs"], xy=(df_Type.loc[i, "dD_CH4"], df_Type.loc[i, "d13C_CH4"]), xytext=(-3,5), textcoords='offset points', fontsize=12)

# Literature_ Plotting
for country, color, label, alpha in [
    # ("New Caledonia", "cornflowerblue", "NC (Literature)", 1),
    ("Oman", "grey", "Oman", 1),
    ("UAE", "aqua", "UAE", 0.7),
    ("Japan", "darkorchid", "Japan", 1),
    ("Philippines", "orange", "Philippines", 1),
    ("Turkey", "lightcoral", "Turkey", 1)]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country
    ax.scatter(
        dflitdata.loc[mask, "dD_CH4"],        # Filtered x-values
        dflitdata.loc[mask, "d13C_CH4"],      # Filtered y-values
        marker="o", s=35, color=color, alpha= alpha, zorder= 4)

plt.xlim(-450, 0)
plt.ylim(20, -90)


# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1)
    
# plt.title("δD_CH4 vs δ13C_CH4", fontweight= "bold")
plt.xlabel("δD($\mathbf{CH_4}$) (‰ VSMOW)", fontweight='bold', fontsize= 13)
plt.ylabel("δ$\mathbf{^{13}C(CH_4)}$ (‰ VSMOW)", fontweight='bold', fontsize= 13)

legend= plt.legend(loc= "lower left", fontsize= 9.5, facecolor= "white", ncol=2, handletextpad=0.0001)
# for text in legend.get_texts():
#     text.set_color('white')

# Annotating figure number
plt.annotate("A", xy=(-20, -88), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)

plt.savefig('dD_CH4vsd13C_CH4_NewCaledonia.svg', format='svg', bbox_inches='tight')
plt.show()