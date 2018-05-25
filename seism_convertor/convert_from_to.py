from obspy import read
from os import listdir
from os.path import isfile, join

# Конвертирует все файлы в папке inputfolder из формата from_ в формат to_
# inputfolder: папка где хранятся файлы формата from_
# outfolder: папка где будут храниться файлы формата to_
def convert_from_to(inputfolder: str, outputfolder: str, from_, to_):
    filenames = [f for f in listdir(inputfolder) if isfile(join(inputfolder, f))]
    sac = [read("./"+inputfolder+"/"+f, debug_headers=True) for f in filenames]
    [s.write((outputfolder+"/"+fname).replace(from_, to_), format='MSEED') for fname, s in zip(filenames, sac)]
