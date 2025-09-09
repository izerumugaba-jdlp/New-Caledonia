# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:12:22 2024

@author: jdlpizerumug
"""

import pandas as pd
import matplotlib.pyplot as plt
import ternary

# Reading data from the Excel file
dfmajorsNC = pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Compilation_rawdata_NC_2019_2020_2022.xlsx",
                           sheet_name= "dataraw_ordered")
dflitdata= pd.read_excel(r"C:\Users\jdlpizerumug\Documents\DOCS_msi\PhD@UniPau\ACADEMICS\NewCaledonia_article\Literaturedata.xlsx", 
                         sheet_name= "Serpent.Contexts_plot" , index_col="IDss")


# Creating a Matplotlib figure with the desired size
fig = plt.figure(figsize=(9, 7))  # Set figure size (width, height)

# Creating the ternary subplot
tax = ternary.TernaryAxesSubplot(scale=100, ax=fig.add_subplot(111))

# Drawing gridlines
tax.gridlines(multiple=10, color="grey", linestyle= '--', linewidth=0.8)

# Customizing the axis line width
tax.boundary(linewidth=1)  # Adjust the width of boundary lines

# Customizing ticks
tax.ticks(axis='lbr', linewidth=1, tick_formats="%.0f", ticks=[0, 20, 40, 60, 80, 100])

# Customizing the axes and fill color
tax.get_axes().set_axisbelow(True)  # Set the axes below the data points

# dflitdata.replace("nan", 0, inplace=True)



# PLOTTING LITERATURE DATA
# Color_map_literature

country_keys_map= {
    "New Caledonia": {"color": "cornflowerblue", "label": "NC (Literature)"}, 
    "Oman": {"color": "grey", "label": "Oman"},
    "UAE": {"color": "aqua", "label": "UAE"},
    "Philippines": {"color": "orange", "label": "Philippines"}, 
    "Turkey": {"color": "lightcoral", "label": "Turkey"},
    "Japan": {"color": "violet", "label": "Japan"},
    "zThis study": {"color": "none", "label": " $This$ $study$ $(NC)$ "}
    }

# Normalisation of CH4, H2, N2 to 100% for a ternary mixture
dflitdata["CH4_t_l"]= (dflitdata["CH4"] / (dflitdata["CH4"]+dflitdata["N2"]+dflitdata["H2"]))*100
dflitdata["N2_t_l"]= (dflitdata["N2"] / (dflitdata["CH4"]+dflitdata["N2"]+dflitdata["H2"]))*100
dflitdata["H2_t_l"]= (dflitdata["H2"] / (dflitdata["CH4"]+dflitdata["N2"]+dflitdata["H2"]))*100
dflitdata["Total_t_l"]= dflitdata["CH4_t_l"] + dflitdata["N2_t_l"] + dflitdata["H2_t_l"]

print(dflitdata[["CH4_t_l", "N2_t_l", "H2_t_l", "Total_t_l"]])


for country, group in dflitdata.groupby("Country"):            
            
    tax.scatter(
        group[["CH4_t_l", "H2_t_l", "N2_t_l"]].values,  # Ensure the order is [CH4, H2, N2_ right, top, left]
        marker="o",
        s=35,
        color= country_keys_map[country].get ("color", "blue"),
        label= country_keys_map[country].get ("label", "blue") if country != "Japan" else None,
        zorder= 2)
    

# PLOTTING THE DATA OF THIS STUDY

site_keys_map = {
    "b.Fanama": {"color": "brown", "marker": "H", "label": "Fanama"},
    "b.La Crouen River": {"color": "brown", "marker": "P", "label": "La Crouen River"},
    "b.Mokoué River": {"color": "brown", "marker": "<", "label": "Mokoué River"},
    "b.Nemwegi": {"color": "brown", "marker": "D", "label": "Nemwegi"},

    "o.Tiebaghi Tunnel": {"color": "forestgreen", "marker": ">", "label": "Tiebaghi Tunnel"},
    "o.Bains des Japonais": {"color": "forestgreen", "marker": "o", "label": "Bains des Japonais"},
    "o.Bains des Kaoris": {"color": "forestgreen", "marker": "X", "label": "Bains des Kaoris"},
    "o.La Coulée River": {"color": "forestgreen", "marker": "p", "label": "La Coulée River"},
    "o.Lembi River": {"color": "forestgreen", "marker": "d", "label": "Lembi River"},
    "o.Les Pirogues River": {"color": "forestgreen", "marker": "*", "label": "Les Pirogues River"},
    "o.Poco Mie": {"color": "forestgreen", "marker": "v", "label": "Poco Mie"},
    "o.Pourina": {"color": "forestgreen", "marker": "s", "label": "Pourina"},
}

# Fixed size for the data points
marker_size = 80

# Normalisation of CH4, H2, N2 to 100% for a ternary mixture
dfmajorsNC["CH4_t"]= (dfmajorsNC["CH4"] / (dfmajorsNC["CH4"]+dfmajorsNC["N2"]+dfmajorsNC["H2"]))*100
dfmajorsNC["N2_t"]= (dfmajorsNC["N2"] / (dfmajorsNC["CH4"]+dfmajorsNC["N2"]+dfmajorsNC["H2"]))*100
dfmajorsNC["H2_t"]= (dfmajorsNC["H2"] / (dfmajorsNC["CH4"]+dfmajorsNC["N2"]+dfmajorsNC["H2"]))*100
dfmajorsNC["Total_t"]= dfmajorsNC["CH4_t"] + dfmajorsNC["N2_t"] + dfmajorsNC["H2_t"]

print(dfmajorsNC[["CH4_t", "N2_t", "H2_t", "Total_t"]])

# Scatter points for each site (grouped per site)
for site, group in dfmajorsNC.groupby("Site"):
    tax.scatter(
        group[["CH4_t", "H2_t", "N2_t"]].values,  # Ensure the order is [CH4, H2, N2_ right, top, left]
        marker= site_keys_map[site].get("marker", "o"),
        color= site_keys_map[site].get("color", "blue"),  
        label= site_keys_map[site].get("label", "newsite"),
        s=marker_size,
        zorder=3  # Set a high z-order to bring points in front
    )

# Setting axis labels
tax.right_corner_label("$\mathbf{CH_4}$", fontsize=15, offset=0.08)  # CH4 in the right corner
tax.top_corner_label("$\mathbf{H_2}$", fontsize=15, offset=0.17)  # H2 at the bottom
tax.left_corner_label("$\mathbf{N_2}$", fontsize=15, offset=0.08)  # N2 in the left corner


# Updating layout for the legend
legend= plt.legend(fontsize=9.3, loc='upper left', bbox_to_anchor=(-0.05, 1.06)) #title="Site", 
legend.set_zorder(-1)

# Setting background color on whole graph
fig.patch.set_facecolor("white")

# Setting background fill color inside the ternary plot
tax.set_background_color(color="white")  # Customize fill inside the ternary triangle

# Removing unwanted cartesian-style ticks, axes, ...! 
plt.gca().set_xticks([])  # Remove x-ticks
plt.gca().set_yticks([])  # Remove y-ticks
plt.gca().spines['top'].set_visible(False)  # Remove top border
plt.gca().spines['right'].set_visible(False)  # Remove right border
plt.gca().spines['left'].set_visible(False)  # Remove left border
plt.gca().spines['bottom'].set_visible(False)  # Remove bottom border

# Saving the plot as an SVG file
plt.savefig("ternary_plot_raw_NC.svg", format='svg', bbox_inches='tight')

# Displaying the plot
tax.show()