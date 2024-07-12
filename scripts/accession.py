import glob
from pathlib import Path
import re
import os
 
root_dir = "./_retro_collection"

DEFAULT_LOCATION = "thirdnerd_hq"
DEFAULT_STATUS = "mostly working"
DEFAULT_TEXT = "lorem ipsum"

# Compute next accession number
p = re.compile(r'R([0-9]*).md')
computed_accession_number = int(sorted([re.search(p, f).group(1) for f in glob.glob('*-R*.md', root_dir=root_dir)], reverse=True)[0]) + 1

# Gather accession info
looping = True

while(looping):
    accession_number = input(f'Accession number [{computed_accession_number}]: ') or computed_accession_number
    location = input(f'Location [{DEFAULT_LOCATION}]: ') or DEFAULT_LOCATION
    manufacturer = input(f'Manufacturer: ')
    model = input(f'Model: ')
    serial = input(f'Serial: ')
    status = input(f'Status [{DEFAULT_STATUS}]: ') or DEFAULT_STATUS
    text = input(f'Text [{DEFAULT_TEXT}]: ') or DEFAULT_TEXT

    print(f'\nAccession number: {accession_number}')
    print(f'Location: {location}')
    print(f'Manufacturer: {manufacturer}')
    print(f'Model: {model}')
    print(f'Serial: {serial}')
    print(f'Status: {status}')
    print(f'Text: {text}')
   
    looping = input('Is this correct [y/n]? ').strip() != 'y'

# Generate template file.
filename = f"{manufacturer.replace(' ', '-')}-{model.replace(' ', '-')}-R{accession_number}.md"

content = f'''---
layout: default
accession: R{accession_number}
location: {location}
manufacturer: {manufacturer}
model: {model}
serial: {serial}
status: {status}
---

{text}
'''

print(f"Creating new accession item {filename}")
(Path.cwd() / root_dir / filename).write_text(content, encoding="utf-8")
