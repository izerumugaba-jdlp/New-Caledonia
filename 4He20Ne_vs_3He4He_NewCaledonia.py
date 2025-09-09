# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 21:44:38 2025

@author: jdlpizerumug
"""

# 4He/20Ne vs 3He/4He _ Plot of mixing between Air, Crust and Mantle endmembers

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Importing files
dfdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx", 
                          index_col= "IDss")  
dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx",
                         sheet_name="Serpent.Contexts_plot", index_col="Sample")
                         
dfendmembers= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\python_phD\endmembers.xlsx")

# Fixed end-member values
Ra= 1.4e-06
Conversion_factor_4He_cm3_g= 1.79e-04    #1 cm3 of 4He at STP= 1.79e-04 g of 4He

# Air
He_air = 5.24e-06    #mol/mol
He3_He4_air = 1 * Ra
He4_Ne20_air = 0.318

# Crust
He_crust_ccg= 5e-05                                          #cm3/g (Martelli et al., 2004)
He_crust= He_crust_ccg * Conversion_factor_4He_cm3_g      #8.95e-09
print(f"He_crust_gg= {He_crust:.2e}")  

He3_He4_crust= 0.02 *Ra
He4_Ne20_crust = 10000

# Mantle (MORB)
He_morb_ccg= 1.5e-05                                         #cm3/g (Martelli et al., 2004)
He_morb= He_morb_ccg * Conversion_factor_4He_cm3_g        #2.68e-09
print(f"He_morb_gg= {He_morb:.2e}")  

He3_He4_morb= 8 * Ra
He4_Ne20_morb = 10000

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Function for getting isotope concentrations_ He3 and He4; from their ratio and sum(total He)
def get_concs_he3_he4(total, ratio):
    He4 = total / (1 + ratio)
    He3 = ratio * He4
    return He3, He4

# Function for getting Ne20 concentration;
def get_conc_Ne20 (He4_Ne20, He4):
    Ne20= He4 / He4_Ne20
    return Ne20

# Mixing fractions, f is the fraction of air in the mix
f = np.linspace(0, 1, 1000000)

# Getting the concentrations of isotopes in endmembers
He3_air, He4_air = get_concs_he3_he4(He_air, He3_He4_air)
He3_crust, He4_crust = get_concs_he3_he4(He_crust, He3_He4_crust)
He3_morb, He4_morb = get_concs_he3_he4(He_morb, He3_He4_morb)

Ne20_air= get_conc_Ne20 (He4_Ne20_air, He4_air)
Ne20_crust= get_conc_Ne20 (He4_Ne20_crust, He4_crust)
Ne20_morb= get_conc_Ne20 (He4_Ne20_morb, He4_morb)

#--------------------------------------------------------------------------------------------------------------------------------------------

# MIXING BTN AIR AND CRUST
# Performing mixing air-crust (ac) i.e calculating isotopes concentration at each step of the mixture
He3_mix_ac = (f * He3_air) + ((1 - f) * He3_crust)
He4_mix_ac = (f * He4_air) + ((1 - f) * He4_crust)
Ne20_mix_ac = (f * Ne20_air) + ((1 - f) * Ne20_crust)

# Computing ratios at each step of of the mixture
He3_He4_mix_ac = (He3_mix_ac / He4_mix_ac) / Ra
He4_Ne20_mix_ac = (He4_mix_ac / Ne20_mix_ac)

# MIXING BTN AIR AND MORB
# Performing mixing air-morb (am) i.e calculating isotopes concentration at each step of the mixture
He3_mix_am = (f * He3_air) + ((1 - f) * He3_morb)
He4_mix_am = (f * He4_air) + ((1 - f) * He4_morb)
Ne20_mix_am = (f * Ne20_air) + ((1 - f) * Ne20_morb)

# Computing ratios at each step of of the mixture
He3_He4_mix_am = (He3_mix_am / He4_mix_am) / Ra
He4_Ne20_mix_am = (He4_mix_am / Ne20_mix_am)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# PLOTTING
fig, ax = plt.subplots()     #(figsize=(10, 6))
# ax.scatter(dfdata["4He/20Ne"], dfdata["R/Ra"], marker="D", s=50, color="blue", label="This study", zorder= 4)

# Plotting endmembers
dfendmembers_f= dfendmembers.drop([2, 11])           #dropping indices whose data i dont wanna show on the plot
endmembers= ax.scatter(dfendmembers_f.loc[:,"4He/20Ne"],dfendmembers_f.loc[:,"R/Ra"], marker= "*", color= "red", s=100, label= "Endmembers")

# THIS STUDY

# sorting the data 
dfdata_South = dfdata[dfdata['Group'] == 'South']
dfdata_North = dfdata[dfdata['Group'] == 'North']

# plotting the data 
Northern_sites= ax.scatter(dfdata_North["4He/20Ne"], dfdata_North["R/Ra"], marker= "D", s=50, color= "brown", label="Northern sites", zorder= 5)
Southern_sites= ax.scatter(dfdata_South["4He/20Ne"], dfdata_South["R/Ra"], marker= "D", s=50, color= "forestgreen", label="Southern sites", zorder= 5)

# Erro bars to the data
plt.errorbar(dfdata.loc[:,"4He/20Ne"], dfdata.loc[:,"R/Ra"], xerr= dfdata.loc[:,"d_4He/20Ne"], yerr= dfdata.loc[:,"d_R/Ra"], capsize=3,  
              fmt= "o", c= "black", markersize= 7)

# Annotating the data
for i in dfdata.index:       
    if i in ["L1B"]:
        ax.annotate(dfdata.loc[i,"IDCs"], xy=(dfdata.loc[i,"4He/20Ne"], dfdata.loc[i,"R/Ra"]), 
                            fontsize= 11, xytext=(-10, 3.5), textcoords='offset points', zorder= 5)
    elif i in ["Co1B"]:
        ax.annotate(dfdata.loc[i,"IDCs"], xy=(dfdata.loc[i,"4He/20Ne"], dfdata.loc[i,"R/Ra"]), 
                            fontsize= 11, xytext=(5, -3), textcoords='offset points', zorder= 5)
    else:
        ax.annotate(dfdata.loc[i,"IDCs"], xy=(dfdata.loc[i,"4He/20Ne"], dfdata.loc[i,"R/Ra"]), 
                            fontsize= 11, xytext=(1, 3.5), textcoords='offset points', zorder= 5)

# LITERATURE_ PLOTTING
for country, color, label in [
    ("New Caledonia", "cornflowerblue", "N.C (Lit.))"),
    ("Oman", "grey", "Oman"),
    ("Philippines", "orange", "Philippines"),
    ("Turkey", "lightcoral", "Turkey")]:
    
    mask = dflitdata["Country"] == country  # Filter data for the current country
    ax.scatter(
        dflitdata.loc[mask, "4He/20Ne"],  # Filtered x-values
        dflitdata.loc[mask, "R/Ra"],      # Filtered y-values
        marker="o", s=35, color=color, label=label, zorder= 4)

# Plotting mixing curves
plt.plot(He4_Ne20_mix_ac, He3_He4_mix_ac, "k")
plt.plot(He4_Ne20_mix_am, He3_He4_mix_am, "k")

#-------------------------------------------------------------------------------------------------------------------------------------------

# MIXING BTN AIR, and different fractional mixing between CRUST AND MORB
# We go from different mixing ratios, considering the mantle fraction f_m_cm.
# This will result in different values of 3He/4He (Ra), but the 4He/20 remains elevated i.e >1000.
f_m_cm= [i/100 for i in [6, 12, 25, 62]]                   # fraction of mantle in mantle-crust mixture
He3_He4_cm= [(j * He3_He4_morb) + ((1 - j) * He3_He4_crust) for j in f_m_cm]
He3_He4_cm_Ra= [k / Ra for k in He3_He4_cm]
print()
print(f"Mantle fr= {f_m_cm}")
print(f"He_He4_CM= {He3_He4_cm_Ra} Ra")

He_cm= [(i * He_morb) + ((1 - i) * He_crust) for i in f_m_cm]
He4_Ne20_cm= [(i * He4_Ne20_morb) + ((1 - i) * He4_Ne20_crust) for i in f_m_cm]


for He3_He4_cm_1, He_cm_1, He4_Ne20_cm1 in zip(He3_He4_cm, He_cm, He4_Ne20_cm):
    
    # Getting the concentrations of isotopes in endmembers
    He3_cm, He4_cm = get_concs_he3_he4(He_cm_1, He3_He4_cm_1)
    Ne20_cm= get_conc_Ne20 (He4_Ne20_cm1, He4_cm)

    
    # Performing mixing air-cm (am) i.e calculating isotopes concentration at each step of the mixture
    He3_mix_a_cm = (f * He3_air) + ((1 - f) * He3_cm)
    He4_mix_a_cm = (f * He4_air) + ((1 - f) * He4_cm)
    Ne20_mix_a_cm = (f * Ne20_air) + ((1 - f) * Ne20_cm)

    # Computing ratios at each step of of the mixture
    He3_He4_mix_a_cm = (He3_mix_a_cm / He4_mix_a_cm) / Ra
    He4_Ne20_mix_a_cm = (He4_mix_a_cm / Ne20_mix_a_cm)
    
    # Plotting mixing curves
    plt.plot(He4_Ne20_mix_a_cm, He3_He4_mix_a_cm, "k--")

#-------------------------------------------------------------------------------------------------------------------------------------------------


plt.xscale("log")
plt.yscale("log")
plt.xlim(0.1, 4*10000)
plt.ylim(0.01, 1.5*10)
plt.xlabel("$\mathbf{^4He/^{20}Ne}$", fontweight='bold', fontsize= 13) 
plt.ylabel("$\mathbf{^3He/^4He}$ (R/Ra)", fontweight='bold', fontsize= 13)


#Annotating RRa values        
ax.annotate("0.02Ra (Crust)", xy=(1.3*10**3, 0.022), xytext=(1.3*10**3, 0.022), color= 'black')
ax.annotate("0.5Ra", xy=(1.3*10**3, 0.55), xytext=(1.3*10**3, 0.55), color= 'black')
ax.annotate("1Ra (Air)", xy=(1.3*10**3, 1.1), xytext=(0, 0), textcoords='offset points', color= 'black')
ax.annotate("Air", xy=(0.25, 0.5), xytext=(-13, 20), textcoords='offset points', color= 'black')
ax.annotate("2Ra", xy=(1.3*10**3, 2.2), xytext=(1.3*10**3, 2.2), color= 'black')
ax.annotate("5Ra", xy=(1.3*10**3, 5.3), xytext=(1.3*10**3, 5.3), color= 'black')
# ax.annotate("6.1Ra (SCLM)", xy=(1.3*10**3, 4.7), xytext=(1.3*10**3, 4.7), color= 'black')
ax.annotate("8Ra (MORB)", xy=(1.2*10**3, 8.6), xytext=(1.2*10**3, 8.6), color= 'black')

#Annotating mantle portion values
ax.annotate("0%", xy=(1.15*10**4, 0.015), xytext=(1.15*10**4, 0.015), color= 'black')
ax.annotate("6%", xy=(1.15*10**4, 0.5), xytext=(1.15*10**4, 0.5), color= 'black')
ax.annotate("12%", xy=(1.15*10**4, 1), xytext=(1.15*10**4, 1), color= 'black')
ax.annotate("25%", xy=(1.15*10**4, 2), xytext=(1.15*10**4, 2), color= 'black')
ax.annotate("62%", xy=(1.15*10**4, 5), xytext=(1.15*10**4, 5), color= 'black')
ax.annotate("100%", xy=(1.15*10**4, 8), xytext=(1.15*10**4, 8), color= 'black')

# Legend and plot formatting
legend= plt.legend(loc= "lower left", fontsize= 8, ncol= 1, handletextpad=0.01)
legend.set_zorder(-1)
legend.get_frame().set_edgecolor("none")  # Removing border
# legend.get_frame().set_facecolor("none")  # Removing background color

# Increasing the line width of the frame
for spine in plt.gca().spines.values():
    spine.set_linewidth(1)
    
# Formatting tick label values
# Custom formatter function
def custom_log_formatter(tv, pos):                                 # pos is position of tick on the axis, not used here but required by FuncFormatter
    if tv >= 1:
        return f"{tv:.0f}"     # No decimals for values >= 1
    elif tv>0.01 and tv<1:
        return f"{tv:.1f}"     # No decimals for values >= 1
    else:
        return f"{tv:.2f}"     # Two decimals for values < 1

# Apply custom formatter
ax.xaxis.set_major_formatter(FuncFormatter(custom_log_formatter))
ax.yaxis.set_major_formatter(FuncFormatter(custom_log_formatter))

plt.savefig('4He20Ne_vs_3He4He_NewCaledonia.svg', format='svg', bbox_inches='tight')

plt.show()
































































