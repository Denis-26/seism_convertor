# List of seismology formats

AH

CSS

GCF

GSE1

GSE2

KINEMETRICS_EVT

KNET

MSEED

NNSA_KB_CORE

PDAS

PICKLE

Q

REFTEK130

SAC

SACXY

SEG2

SEGY

SEISAN

SH_ASC

SLIST

SU

TSPAIR

WAV

WIN

Y

# Install

```bash
git clone https://github.com/Denis-26/seism_convertor.git
cd ./seism_convertor
sudo pip3 install .
```

# Description

Converts all files in folder **inputfolder** from format **from_** to format **to_**

**inputfolder:** folder where files **from_** format is stored

**outfolder:** folder where files **to_** format will store

# Usage

**You have next project structure**

```
  CSS/
  SAC/
  main.py
```

**main.py**

```python
from seism_convertor.seism_convertor import convert_from_to

def main():
    convert_from_to('SAC', 'CSS', "SAC", "CSS")

if __name__ == '__main__':
    main()
```
