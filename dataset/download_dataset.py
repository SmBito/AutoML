# !wget "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip"

# import copy
import os
from subprocess import call

print("")

print("Downloading...")
if not os.path.exists("kagglecatsanddogs_3367a.zip"):
    call(
        'wget "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip"',
        shell=True
    )
    print("Downloading done.\n")
else:
    print("Dataset already downloaded. Did not download twice.\n")


print("Extracting...")
extract_directory = os.path.abspath("kagglecatsanddogs_3367a")
if not os.path.exists(extract_directory):
    call(
        'unzip -nq "kagglecatsanddogs_3367a.zip"',
        shell=True
    )
    print("Extracting successfully done to {}.".format(extract_directory))
else:
    print("Dataset already extracted. Did not extract twice.\n")
