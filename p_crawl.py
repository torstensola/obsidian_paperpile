import re
import glob
import os

def p_crawl(folder='/Users/torst/Desktop/UiA/Resources/Obsidian notes/Tors notater/'):
    # Open latest MD note names Untitled.md
    list_of_files = glob.glob(folder + '*.md')
    note = max(list_of_files, key=os.path.getctime)
    # Check file
    if note.split('/')[-1] != 'Untitled.md':
        print('Untitled file not located. Try saving!')
        exit()
    print('Using: '.format(note))

    # Get lines from MD file
    with open(note) as f:
        mylist = f.read().splitlines()

    # Make a dictionary with entries
    tdict = dict()
    for line in mylist[2:-1]:  # Exclude empty and nonsense fields
        use_line = re.sub(r'^["{}]+|["{},]+$', '', line.split(' = ')[1])  # Remove unwanted chars at start/end of each field
        tdict[line.split(' = ')[0].capitalize()] = use_line  # keyword-value pairs

    # Fix authors into Obsidian page format
    au_list = ['[[{}]]'.format(i) for i in tdict['Author'].split(' and ')]
    tdict['Author'] = ', '.join(au_list)

    # Fix keywords and make into #compound_tags
    if 'Keywords' in tdict.keys():
        kw_list = ['#{}'.format(i) for i in tdict['Keywords'].split('; ')]
        for i, t in enumerate(kw_list):
            kw_list[i] = re.sub(r'\s', '_', t)

        tdict['Keywords'] = ', '.join(kw_list)
    else:
        tdict['Keywords'] = ''

    # Sort according to preference
    first_keys = [key for key in ['Title', 'Author', 'Journal', 'Year', 'Url', 'Abstract', 'Keywords'] if key in tdict.keys()]
    all_keys = first_keys + [i for i in list(tdict.keys()) if i not in first_keys]
    tdict = {key: tdict[key] for key in all_keys}

    # Generate final text section
    text = ['##### {}\n{}\n\n'.format(key, tdict[key]) for key in tdict.keys()]

    # Write to file
    a_file = open(note, 'w')
    a_file.writelines(text)
    a_file.close()

    # Rename file
    new_name = '{}Paper notes/{} et al{} {}.md'.format(note[:note.rfind('/')+1],
                                                       tdict['Author'].split(',')[0][2:],
                                                       tdict['Year'],
                                                       tdict['Title'])
    os.rename(note, new_name)


p_crawl()