from pygbif import species
import pandas as pd
import argparse
from tqdm.auto import tqdm

# host url of GBIF
url = 'https://www.gbif.org/species/'
'''Every link specie in the GBIF database has an url make up by its database key (speciesKey).
Juanma wants a to get the url of the page of each specie. So I just have to use the url above and 
retrieve the database key with the GBIF's API using the the python app pygbif'''

def read_excel (name, sheet_name='Plantilla'):
    df = pd.read_excel(name, sheet_name, skiprows=1)
    return df

def retrieve_key (name, url):
    if len(name.strip().split(" ")) > 1:
        try:
            key = species.name_backbone(name)['speciesKey']
            return url + str(key)
        except:
            return ""
    return ""

if __name__ == '__main__':

    ## Parse arguments
    parser = argparse.ArgumentParser(
                    prog='gbifSpecieLinkConstructor',
                    description='''Receives an excel with a column with species names and 
                    generates an excel with species names and their respective links to the GBIF web page.''',
                    epilog='Author: Juan Picon')
    parser.add_argument('excelname', help='An excel file with a column for species name ')
    parser.add_argument('-o','--output', help='Name for the output file')
    args = parser.parse_args()
    excel_name_input = args.excelname 
    excel_name_output = "gbif_link_constructor_out.xlsx" if args.output == None  else (args.output + ".xlsx")
    
    # Read excel input
    df = read_excel(excel_name_input)
    # Select necessary columns
    df = df [["Nombre científico","ID del nombre científico"]]
    ### progress bar ###
    tqdm.pandas(desc="Species collected")
    # Add link to the column of urls
    df["ID del nombre científico"] = df ["Nombre científico"].progress_apply(lambda name: retrieve_key(name, url))
    # Excel final
    df.to_excel(excel_name_output, sheet_name="Plantilla_url")
    
    
