
# Unzip the dataset

# !pip install patool

from patoolib import extract_archive
import os

zipfile = 'ckplus.zip'

extract_to = 'ckplus'

os.mkdir(extract_to) 

extract_archive(zipfile, outdir=extract_to)
