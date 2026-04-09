muH2=-31.818789868560483
muH2O=-468.4472305388307
muO2=-866.6727604533233

muZnO_Cu=-5550.93343772379*27.2114
muZnS_Cu=-6851.6424715489*27.2114
muZnSe_Cu=-6777.56378357231*27.2114

muZnO=-5563.881992*27.2114
muZnS=-6864.59368219198*27.2114
muZnSe=-6790.5153695988*27.2114

muZnOCu_H2O_ads=-151518.10185170427
muZnSCu_H2O_ads=-186910.6294842915
muZnSeCu_H2O_ads=-184894.79660432605

DeltaG_ads_ZnO_Cu= muZnOCu_H2O_ads - muH2O - muZnO_Cu
DeltaG_ads_ZnS_Cu= muZnSCu_H2O_ads - muH2O - muZnS_Cu
DeltaG_ads_ZnSe_Cu= muZnSeCu_H2O_ads - muH2O - muZnSe_Cu
DeltaG_ads_ZnO= muZnO_H2O_ads - muH2O - muZnO
DeltaG_ads_ZnS= muZnS_H2O_ads - muH2O - muZnS
DeltaG_ads_ZnSe= muZnSe_H2O_ads - muH2O - muZnSe

print(DeltaG_ads_ZnO_Cu)
print(DeltaG_ads_ZnS_Cu)
print(DeltaG_ads_ZnSe_Cu)



#-0.984473888296634 per ZnO dopato
#0.601696553057991 per ZnS dopato
#0.6497665123315528 per ZnSe dopato
