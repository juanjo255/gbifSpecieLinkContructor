# gbifSpecieLinkContructor
* This tool is to build the species url of the GBIF web page that describes it.
* The program expect an excel file with two columns named named: "Nombre científico" and "ID del nombre científico". Where "Nombre científico" correspond to the column with the species and "ID del nombre científico" an empty column where the species url from the GBIF will be stored. You can find an example in the folder "Dataset_examples ->  "DwC_D&L_EGF_Mutata-Carepa_20230608.xlsx".

## Installation

**First step:** Clone this repository

`git clone https://github.com/juanjo255/gbifSpecieLinkContructor.git && cd gbifSpecieLinkContructor`

**Second step:** Install requirements

You must have installed Python (tested on `Python >= 3.9.16`). The recommended option is through [Conda](https://docs.conda.io/en/latest/miniconda.html).

* Using Conda:

`conda create -n gbif pip && conda activate gbif`

* After you install Python by your method of preference run:

`pip install -r requirements.txt`

**Third step:** Run the program

* To run the program is just as simple as: 

`python gbifSpecieLinkContructor.py path_to_dataset`

The default path to save the output file is the working directory.

* To print the help message on the options available

`python gbifSpecieLinkContructor.py --help`
