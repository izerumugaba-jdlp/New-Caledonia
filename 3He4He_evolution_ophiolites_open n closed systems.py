# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:44:31 2025

@author: jdlpizerumug
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# THE FOLLOWING EQUATION CAN REPRESENT THE 3He/4He SIGNATURE EVOLUTION WITH TIME
# (4He/3He_start * F_3He * t0) + (JHe *t) = 4He/3He_ophioliteage * F_3He * t0

JHe= 1.0e+06                                  #atoms_He4 m-2 s-1 #4He Flux (calculated based on the content in U (0.001), Th(0.002); and 4He generating thickness (2km)!!)

Ra= 1.4e-06
RRa_start_closed= 6.9
RRa_start_open= 8
F_3He_min= 10000                              # atoms 3He m-2 s-1 (3He flux in the obducted ophiolite. ref flux observed in continents is <10000atoms m-2 s-1. Day et al., 2015 after Sano, 1986; Ballentine, 1997
F_3He_max= 40000                              # atoms 3He m-2 s-1 (3He flux in oceanic crust; ref)

t0= 1                                         # Ma
tmax= 250
t= np.arange(0, tmax, 0.001)                  # Ma
age_oph= 40

RRa_start= [RRa_start_closed, RRa_start_open]                                  # Starting mantle (i.e ophilite) signature (3He/4He (Ra)); closed n open systems

for i in RRa_start:
    He4He3_start= 1 / (i * Ra) 

    # GENERAL EQUATION RRa VS t
    # F_3He_min
    He4He3_t_Fmin= ((He4He3_start * F_3He_min * t0) + (JHe * t)) / (F_3He_min * t0)
    RRa_t_Fmin= (1 / He4He3_t_Fmin) / Ra

    # F_3He_max
    He4He3_t_Fmax= ((He4He3_start * F_3He_max * t0) + (JHe * t)) / (F_3He_max * t0)
    RRa_t_Fmax= (1 / He4He3_t_Fmax) / Ra

    # FOR t= AGE_OPHIOLITE
    # F_3He_min
    He4He3_oph_Fmin= ((He4He3_start * F_3He_min * t0) + (JHe * age_oph)) / (F_3He_min * t0)
    RRa_oph_Fmin= (1 / He4He3_oph_Fmin) / Ra

    # F_3He_max
    He4He3_oph_Fmax= ((He4He3_start * F_3He_max * t0) + (JHe * age_oph)) / (F_3He_max * t0)
    RRa_oph_Fmax= (1 / He4He3_oph_Fmax) / Ra

    print("FOR AN OPEN SYSTEM - EVOLVED OLM") if i== RRa_start_open else print ("FOR A CLOSED SYSTEM - EVOLVED OLM")
    print("---------------------------------")
    print(f"* RRa_oph_Fmin= {round(RRa_oph_Fmin, 2)} #RRa at t= {age_oph} Ma; F_3He_oph= {F_3He_min}, RRa_start= {i}\n")
    print(f"* RRa_oph_Fmax= {round(RRa_oph_Fmax, 2)} #RRa at t= {age_oph} Ma; F_3He_oph= {F_3He_max}, RRa_start= {i}\n")

    # HOW LONG WOULD IT TAKE FOR THE OPHIOLITE TO REACH A GIVEN RRa VALUE? SAY THE CRUSTAL_SIGNATURE= 0.02Ra, or 0.5 - 1.5Ra, the range of values to which a mixture with 50% air would result in an air-like signature
    # transforming the formula; t= ((4He/3He_ophioliteage * F_3He * t0) - (4He/3He_start * F_3He * t0)) / JHe
    target_RRa= 1.5
    target_He4He3= (1 / (target_RRa * Ra))
    t_trgt_RRa_Fmin= ((target_He4He3 * F_3He_min * t0) - (He4He3_start * F_3He_min * t0)) / JHe
    t_trgt_RRa_Fmax= ((target_He4He3 * F_3He_max * t0) - (He4He3_start * F_3He_max * t0)) / JHe

    print(f"* t_{target_RRa}_Fmin= {round(t_trgt_RRa_Fmin, 2)} Ma #target_RRa= {target_RRa}; F_3He_oph= {F_3He_min}, RRa_start= {i}\n")
    print(f"* t_{target_RRa}_Fmax= {round(t_trgt_RRa_Fmax, 2)} Ma #target_RRa= {target_RRa}; F_3He_oph= {F_3He_max}, RRa_start= {i}\n")
    print()
    
    # Plotting
    if i== RRa_start_open:
        plt.plot(t, RRa_t_Fmin, "g--", linewidth= 3, label= f"OLM: open; F_3He_oph : {F_3He_min}", zorder= 0)
        plt.plot(t, RRa_t_Fmax, "g", linewidth= 3, label= f"OLM: open; F_3He_oph : {F_3He_max}")
    elif i== RRa_start_closed:
        plt.plot(t, RRa_t_Fmin, "b--", linewidth= 3, label= f"OLM: closed; F_3He_oph :{F_3He_min}", zorder= 0)
        plt.plot(t, RRa_t_Fmax, "b", linewidth= 3, label= f"OLM: closed; F_3He_oph : {F_3He_max}")

# Plot annotation
plt.plot ((age_oph, age_oph),(0, 9), "k--", label= (f"Age after obduction = {age_oph} Ma"))
plt.xlim(0, tmax)
plt.ylim(0, 9)
plt.xlabel("Age (Ma)", fontweight= 'bold', fontsize= 13)
plt.ylabel("$\mathbf{^3He/^4He}$ (R/Ra)", fontweight= 'bold', fontsize= 13)
plt.legend(fontsize= 10)
    
# saving the figure
plt.savefig('3He4He_evolution_ophiolites_open&closed systems_NC.svg', format='svg', bbox_inches='tight')

plt.show()






