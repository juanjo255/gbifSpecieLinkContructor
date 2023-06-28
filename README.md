# gbifSpecieLinkContructor
This tool is to build the species url of the GBIF web page that describes it.

## Installation

**First step:** Clone this repository

`git clone https://github.com/juanjo255/gbifSpecieLinkContructor.git && cd gbifSpecieLinkContructor`

**Second step:** Install requirements

You must have installed python (it works on python `>= 3.9.16`). The recommended option is through [Conda](https://docs.conda.io/en/latest/miniconda.html)

`pip install -r requirements.txt`

**Third step:** Run the program

* To run the program is just as simple as: 

`python gbifSpecieLinkContructor.py path_to_dataset`

The default path to save the output file is the working directory.

* To print the help message on the options available

`python gbifSpecieLinkContructor.py --help`
