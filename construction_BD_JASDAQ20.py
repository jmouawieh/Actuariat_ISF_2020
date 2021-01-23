import glob
import os
import pandas as pd

#liste des base de données du JASDAQ 20 (output :list_df_JASDAQ20 )
List_Company = ['AsianTech', 'Broccoli','Crooz','Ferrotec', 'Harmonic', 'MacDoJP', 'MeikoElec', 'Nakanishi',
               'Septeni', ' Seria', 'Shinoken', 'TanakaChem', 'ThineElec', 'Toyo', 'Ubiquitous', 'Universal'
               , 'Vector', 'West', 'Workman', 'Yumeshin']
import glob
import os

path = "/Users/jadmwh/Desktop/JASDAQ 20" # mon fichier avec les CSV
all_files = glob.glob(path + "/*.csv") #liste des nom de chemin vers les bases de données
all_files.sort(key=os.path.getmtime)
list_df_JASDAQ20 = []

for company, filename in zip(List_Company, all_files):
    company = pd.read_csv(filename, index_col=None, header=0)
    list_df_JASDAQ20.append(company)

date = list_df_JASDAQ20[0].drop(["Dernier","Ouv.","Plus Haut","Plus Bas","Vol.","Variation %"], axis=1) # pour ensuite conserver que les prix journalier de chaque titre

#uniformise les noms de colonnes (car certaine table sont en anglais)
list_df_JASDAQ20[1].columns= ["Date","Dernier","Ouv.","Plus Haut","Plus Bas","Vol.","Variation %"]
list_df_JASDAQ20[2].columns= ["Date","Dernier","Ouv.","Plus Haut","Plus Bas","Vol.","Variation %"]
list_df_JASDAQ20[3].columns= ["Date","Dernier","Ouv.","Plus Haut","Plus Bas","Vol.","Variation %"]
list_df_JASDAQ20[4].columns= ["Date","Dernier","Ouv.","Plus Haut","Plus Bas","Vol.","Variation %"]

#on conserve que les prix
for i in range(len(list_df_JASDAQ20)):
    list_df_JASDAQ20[i].drop(["Date","Ouv.","Plus Haut","Plus Bas","Vol.","Variation %"], axis=1, inplace = True)
#on renome chaque colonne par le nom de l'entreprise
for i in range(len(list_df_JASDAQ20)):
    list_df_JASDAQ20[i].columns = [List_Company[i]]

#enfin on passe a la concatenation la liste des dates et du prix journalier pour chaque entreprise
df_JASDAQ20_initial = pd.concat(list_df_JASDAQ20, axis=1)
df_JASDAQ20_initial =pd.concat([date, df_JASDAQ20_initial], axis=1)

#conversion des en float (certain chiffres sont en norme anglaises et d'autre francaises)
for company in ['AsianTech', 'Broccoli','Crooz','Ferrotec', 'Harmonic', 'MacDoJP', 'MeikoElec', 'Nakanishi',
               'Septeni', ' Seria', 'Shinoken', 'TanakaChem', 'ThineElec', 'Toyo', 'Ubiquitous', 'Universal'
               , 'Vector', 'West', 'Workman', 'Yumeshin']:
    if company in ['Broccoli','Crooz','Ferrotec', 'Harmonic', 'MacDoJP']:
         df_JASDAQ20_initial[company] = df_JASDAQ20_initial[company].str.replace(",", "", regex =True)
    else:
        df_JASDAQ20_initial[company] = df_JASDAQ20_initial[company].str.replace(".", "", regex =True)
        df_JASDAQ20_initial[company] = df_JASDAQ20_initial[company].str.replace(",", ".", regex =True)
    df_JASDAQ20_initial[company]=pd.to_numeric(df_JASDAQ20_initial[company])
    
df_JASDAQ20_initial["Date"]=pd.to_datetime(df_JASDAQ20_initial["Date"])#arranger le format date
df_JASDAQ20_initial=df_JASDAQ20_initial.iloc[::-1]
df_JASDAQ20_initial.dtypes

df_JASDAQ20_initial.to_csv("/Users/jadmwh/Desktop/JASDAQ 20/JASDAQ20_ini.csv", index= False)


#test de corrélation entre workman et JASDAQ 20 --> -0.08893721692098412

#importation des prix de clotures du JASDAQ 20
df_JASDAQ20= pd.read_csv("/Users/jadmwh/Downloads/JASDAQ 20 - Données Historiques (1).csv")
#selection des colonnes
df_JASDAQ20.drop(["Ouv.","Plus Haut","Plus Bas","Vol.","Variation %"],axis = 1, inplace = True)
df_JASDAQ20["Dernier"] = df_JASDAQ20["Dernier"].str.replace(".", "", regex =True)
df_JASDAQ20["Dernier"] = df_JASDAQ20["Dernier"].str.replace(",", ".", regex =True)
df_JASDAQ20["Dernier"] =pd.to_numeric(df_JASDAQ20["Dernier"] )
df_JASDAQ20.columns = ["Date","JASDAQ20"]
df_JASDAQ20["Date"] = pd.to_datetime(df_JASDAQ20["Date"])
df_JASDAQ20=df_JASDAQ20.iloc[::-1]
df_JASDAQ20

#test de corrélation
pd.concat([df_JASDAQ20_initial["Workman"], df_JASDAQ20["JASDAQ20"]], axis=1, keys=['Workman', 'JASDAQ20']).corr().loc['JASDAQ20', 'Workman']
