# TODO

# replace ```<language> with ```<magic> and remove magics
import shutil
import os
from nbconvert import MarkdownExporter, SlidesExporter
from nbconvert.preprocessors import TagRemovePreprocessor
import re
from glob import glob

nbs = glob(r'notebooks/*.ipynb')
print(nbs)
md_exclusions = []
rv_exclusions = [r'notebooks/pop-quiz.ipynb']

md_nbs = [nb for nb in nbs if nb not in md_exclusions]
rv_nbs = [nb for nb in nbs if nb not in rv_exclusions]

tr_pp = TagRemovePreprocessor(remove_cell_tags=['remove'], remove_input_tags=['remove-input'])
md_exp = MarkdownExporter(preprocessors=[tr_pp])
rv_exp = SlidesExporter(exclude_input_prompt=True, reveal_theme='white', reveal_scroll=True, preprocessors=[tr_pp])

for nb in rv_nbs:
    nb_name = nb.rsplit(r'/')[1].split('.')[0]
    slides_dest = f'docs/{nb_name}-slides.html'

    if os.path.exists(slides_dest):
        os.remove(slides_dest)

    
# #copy images folder

source_dir = r'notebooks/images/'
target_dir = r'docs/images/'
file_names = os.listdir(source_dir)

for file_name in file_names:
    try:
        shutil.copy(os.path.join(source_dir, file_name), target_dir)
    except:
        pass

#copy custom.css
try:
    shutil.copy('notebooks/custom.css', 'docs/custom.css')
    print('custom.css copied to docs/')
except:
    pass

#markdown
regex = re.compile(r"```(\n)+((\ {4,}?.+(\n+))+)\n")
prefix = '\n\n```{.python .nb-output}\n'
suffix = '\n```\n\n'
prefix_offset = 3
suffix_offset = 0
max_matches = None
start_index = 0

for nb in md_nbs:

    text, resources = md_exp.from_file(nb)
    md_file_dest = f'docs/{nb[10:-6]}.md'
    
    matches = re.finditer(regex, text)
    locations = []
    for match in matches:
        start = match.start()
        end = match.end()
        locations.append((start, end))    

    destinations = [(location[0] + prefix_offset, location[1] + suffix_offset) for location in locations][:max_matches]

    new = []
    
    text_pos = start_index
    for dest in destinations:
        prefix_pos = dest[0]
        suffix_pos = dest[1]
        replacement_string = text[prefix_pos:suffix_pos].strip("\n")#specific to this scenario
        new.append(f'{text[text_pos:prefix_pos]}{prefix}{replacement_string}{suffix}')
        text_pos = suffix_pos
    new.append(text[text_pos:])
        
    new_text = ''.join(new)
    
    # add slides link if in rv_nbs
    if nb in rv_nbs:
        url = f"../{md_file_dest.rsplit('/')[1].split('.')[0]}-slides.html"

        with open('header.txt', 'r') as f:
            header = f.read()
            
        header = header.replace('xxSLIDES_URLxx', url)
    
    else: 
        header = ''

    with open(md_file_dest, 'w') as f:
        
        f.write(header)
        f.write(new_text)

    print(f'{md_file_dest} created, {len(destinations)} regex matches processed.')


#Slides
for nb in rv_nbs:
    
    text, resources = rv_exp.from_file(nb)
    
    nb_name = nb.rsplit(r'/')[1].split('.')[0]
    slides_dest = f'docs/{nb_name}-slides.html'

    text = text.replace(r'{target=_blank}','')
    text = text.replace(r'{.adios}','')


    with open(slides_dest, 'a') as f:
        f.write(text)
        print(f'{slides_dest} created.')
