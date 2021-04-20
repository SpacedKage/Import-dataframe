import pandas as pd

frame = pd.DataFrame([[8.96, 1884], [7.87, 1149], [7.13, 428]],
 index = ["Copper", "Iron", "Zinc"],
 columns = ["Density g/cm3", "Melting Point BC"])

print(frame)
print()
print(frame.loc["Copper"])

# if we were to create a dataframe using the previous method then

metals = {"Metal": ["Copper", "Iron", "Zinc"],
 "Density g/cm3": [8.96, 7.87, 7.13],
 "Melting Point BC": [1884, 1149, 428]}

frame2 = pd.DataFrame(metals)

print (frame2)