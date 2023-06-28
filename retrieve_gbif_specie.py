from pygbif import species
import pandas as pd
url = 'https://www.gbif.org/species/'
'''Every link specie in the GBIF database has an url make up by its database key (speciesKey).
Juanma wants a to get the url of the page of each specie. So I just have to use the url above and 
retrieve the database key with the GBIF's API using the the python app pygbif'''

def read_excel (name):
    df = pd.read_excel(name, sheet_name='Plantilla', skiprows=1)
    return df

df = read_excel('./DwC_D&L_EGF_Mutata-Carepa_20230608.xlsx')
df = df [["Nombre científico","ID del nombre científico"]]
def retrieve_key (name, url):
    if len(name.strip().split(" ")) > 1:
        print("specie: ", name)
        key = species.name_backbone(name)['speciesKey']
        return url + str(key)
    return " "
df["ID del nombre científico"] = df ["Nombre científico"].apply(lambda name: retrieve_key(name, url))
df.to_excel('./specie_urls.xlsx', sheet_name="Plantilla_url")
