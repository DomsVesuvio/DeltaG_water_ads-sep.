muH2=-31.818789868560483
muH2O=-468.4472305388307
muO2=-866.6727604533233

muZnO_Cu=-5550.93343772379*27.2114
muZnS_Cu=-6851.6424715489*27.2114
muZnSe_Cu=-6777.56378357231*27.2114

muZnO=-5563.881992*27.2114
muZnS=-6864.59368219198*27.2114
muZnSe=-6790.5153695988*27.2114



muZnOCu_OH_ads=-151501.20362725505
muZnOCu_H_ads=-151063.28805820455
muZnOCu_H2O_ads=-151518.10185170427

muZnSCu_OH_ads=-186894.26043731655
muZnSCu_H_ads=-186456.03641370084
muZnSCu_H2O_ads=-186910.6294842915

muZnSeCu_OH_ads=-184878.72692001172
muZnSeCu_H_ads=-184439.97319227585
muZnSeCu_H2O_ads=-184894.79660432605

#DeltaG1= muZnO_OH_ads + muZnO_H_ads - muZnO_H2O_ads - muZnO
#DeltaG2= muZnS_OH_ads + muZnS_H_ads - muZnS_H2O_ads - muZnS
#DeltaG3= muZnSe_OH_ads + muZnSe_H_ads - muZnSe_H2O_ads - muZnSe

DeltaG_ZnO_doped= muZnOCu_OH_ads + muZnOCu_H_ads - muZnOCu_H2O_ads - muZnO_Cu
DeltaG_ZnS_doped= muZnSCu_OH_ads + muZnSCu_H_ads - muZnSCu_H2O_ads - muZnS_Cu
DeltaG_ZnSe_doped= muZnSeCu_OH_ads + muZnSeCu_H_ads - muZnSeCu_H2O_ads - muZnSe_Cu

print(DeltaG_ZnO_doped)
print(DeltaG_ZnS_doped)
print(DeltaG_ZnSe_doped)


#DeltaG di ZnO_Cu è  2.2803135217982344
#DeltaG di ZnS_Cu è 3.116583579860162
#DeltaG di ZnSe_Cu è 3.0956323380814865



#Per i basso spin le differenze tra deltaG1 e deltaG(appena calcolati)  da correggere.
#-1.16 ZnOCu; -0.44 per ZnSCu; -0.53 per ZnSeCu


#Per gli alto spin le differenze tra i deltaG1 e i deltaG(appena calcolati)
#-1.35 ZnOCu: -0.36 per ZnSCu ; -0.66 per ZnSeCu.
