# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:42:52 2023

@author: jdlpizerumug
"""

import pandas as pd
import matplotlib.pyplot as plt

dfdataNC= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                        sheet_name="dataraw_ordered", index_col= "IDss")   
dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx", sheet_name="Serpent.Contexts", 
                         index_col="IDss")
dffileendmembers= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\python_phD\fileendmembers.xlsx")  
dfcommonplots= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\python_phD\commonplots.xlsx")
dfendmembers= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\python_phD\endmembers.xlsx")
andesCHe= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\python_phD\AndesC-He_ Barryetal2022.xlsx")

#Methane genesis fields (Milkov and Etiope.; 2018)
#Abiotic
Xabcc= [+9.8, +9.8, +8.5, -2.5, -5.5, -8, -11.5, -18.5, -25, -28.5, -48.5, -50, -50, -43, -27, -25, -19, -4.5, +1, +8, +9.8]
Yabcc= [-3, -9, -12, -34.5, -38, -39, -40, -40, -38.5, -36.5, -22, -21, -19, -14, 0, +1, +2, +2, +1, -1, -3]

#Fermentation (F)
Xfcc= [-90, -70, -59, -55, -52, -50, -50, -53, -67, -68, -69, -70, -90, -90]
Yfcc= [+1, +1, 0, -0.5, -5, -8, -13, -17, -24, -24.5, -25, -24, -13, +1]

#CO2-Reduction (CR)- originated
Xcrcc= [-79.5, -90, -90, -65, -63, -60, -59.5, -59.5, -60, -67, -79.5]
Ycrcc= [-50, -50, -12, +15, +15, +11, +10, -27.5, -30, -41, -50]

#Thermogenic
Xtgcc= [-28.5, -27.5, -25, -20, -18, -16, -16, -18, -30, -40, -42, -53.5, -60, -65, -71, -75, -75, -72.5, -70, -54, -44, -28.5]
Ytgcc= [+11, +11, +9.5, +5.5, +2, -2, -8, -15, -30, -39.5, -40, -40, -38.5, -37, -32, -27.5, -25, -22, -19, -7, +1.5, +11]

#Secondary Microbial (SM)
Xsmcc= [-59, -59, -35, -35, -59]
Ysmcc= [+1, +40, +40, +1, +1]


#PLotting
fig, ax = plt.subplots()
#Fields shapes
ax.plot(Xabcc, Yabcc, color="purple", linewidth=0.7)
ax.plot(Xfcc, Yfcc, color="cornflowerblue", linewidth=0.7)
ax.plot(Xcrcc, Ycrcc, color="royalblue", linewidth=0.7)
ax.plot(Xtgcc, Ytgcc, color="red", linewidth=0.7)
ax.plot(Xsmcc, Ysmcc, color="black", linestyle= "--", linewidth=0.7)
#Fields fill
plt.fill(Xabcc, Yabcc, color= "purple", alpha= 0.1)
plt.fill(Xfcc, Yfcc, color= "cornflowerblue", alpha= 0.1)
plt.fill(Xcrcc, Ycrcc, color= "royalblue", alpha= 0.1)
plt.fill(Xtgcc, Ytgcc, color= "red", alpha= 0.1)
plt.fill(Xsmcc, Ysmcc, color= "black", alpha= 0.1)
#Annotations
ax.annotate("Abiotic", xy=(-18, -20), xytext=(-18, -20), size= 15, color="purple")
ax.annotate("F", xy=(-89, -6), xytext=(-89, -6), size= 15, color="cornflowerblue")
ax.annotate("CR", xy=(-88, -33), xytext=(-88, -33), size= 15, color="royalblue")
ax.annotate("Primary microbial", xy=(-86, -23), xytext=(0, 0), textcoords='offset points', size= 12, color="royalblue", rotation= 40)
# ax.annotate("microbial", xy=(-87, -14), xytext=(-87, -14), size= 15, color="royalblue")
ax.annotate("Thermogenic", xy=(-60, -47), xytext=(-60, -47), size= 15, color="red")
ax.annotate("EMT", xy=(-58, -30), xytext=(-58, -30), size= 15, color="red")
ax.annotate("OA", xy=(-48, -10), xytext=(-48, -10), size= 15, color="red")
ax.annotate("LMT", xy=(-34.5, 0), xytext=(-34.5, 0), size= 15, color="red", alpha= 0.7)
ax.annotate("Secondary", xy=(-59, 25), xytext=(-59, 25), size= 15, color="black")
ax.annotate("Microbial", xy=(-57, 17), xytext=(-57, 17), size= 15, color="black")

# Plotting_ This study
for Type, marker, color, label, zorder in [
        ("Ophiolitic", "D", "green", "Ophiolitic", 5),
        ("Basement", "D", "maroon", "Basement", 6)]:
    df_Type= dfdataNC[dfdataNC["Type"] == Type]
    plt.scatter(df_Type["d13C_CH4"], df_Type["d13C_CO2"], marker= marker, s=70, color= color, label= label, zorder= zorder)

# ax.scatter(dfdataNC.loc[:,"d13C_CH4"],dfdataNC.loc[:,"d13C_CO2"], marker= "D", s= 50, color= "blue", zorder= 5)
plt.xlim(-90, 10)
plt.ylim(-50, 40)
for i in dfdataNC.index:
    if i in ["Nmg1", "Fnm"]:
        ax.annotate(i, xy=(dfdataNC.loc[i,"d13C_CH4"], dfdataNC.loc[i,"d13C_CO2"]), xytext=(-12,-17), textcoords='offset points', fontsize=12)
    elif i in ["Cr"]:
        ax.annotate(i, xy=(dfdataNC.loc[i,"d13C_CH4"], dfdataNC.loc[i,"d13C_CO2"]), xytext=(-8,-17), textcoords='offset points', fontsize=12)
    elif i in ["Mo"]:
        ax.annotate(i, xy=(dfdataNC.loc[i,"d13C_CH4"], dfdataNC.loc[i,"d13C_CO2"]), xytext=(-5,-18), textcoords='offset points', fontsize=12)
    elif i in ["PM1"]:
        ax.annotate(i, xy=(dfdataNC.loc[i,"d13C_CH4"], dfdataNC.loc[i,"d13C_CO2"]), xytext=(-12,8), textcoords='offset points', fontsize=12)    
    else:
        ax.annotate(i, xy=(dfdataNC.loc[i,"d13C_CH4"], dfdataNC.loc[i,"d13C_CO2"]), xytext=(0,5), textcoords='offset points', fontsize=12)

"""
# Literature_ Plotting
for country, color, label in [
    ("New Caledonia", "cornflowerblue", "NCL (Lit))"),
    ("Oman", "grey", "Oman"),
    ("Philippines", "orange", "Philippines"),
    ("Turkey", "lightcoral", "Turkey")]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country
    ax.scatter(
        dflitdata.loc[mask, "d13C_CH4"],        # Filtered x-values
        dflitdata.loc[mask, "d13C_CO2"],      # Filtered y-values
        marker="o", s=35, color=color, label=label, zorder= 4)
"""
        
# plt.title(" δ13C_CH4 vs δ13C_CO2", fontweight= "bold")
plt.xlabel("δ$\mathbf{^{13}C(CH_4)}$ (‰ VPDB)", fontweight='bold', fontsize= 13)
plt.ylabel("δ$\mathbf{^{13}C(CO_2)}$ (‰ VPDB)", fontweight='bold', fontsize= 13)
plt.legend(loc="upper right", fontsize= 11)

# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1)
    
# Annotating figure number
plt.annotate("B", xy=(-87, 38), 
                xytext=(0, 0), ha='center', va='top', textcoords='offset points', fontsize= 20, fontweight= "bold", zorder=6)
    
plt.savefig('d13C_CH4vsd13C_CO2_NewCaledonia.svg', format='svg', bbox_inches='tight')    
plt.show()