import re
from tkinter.messagebox import NO
from typing import Set

CLIPPINGS = 'My Clippings.txt'
PARSED = 'parsed-results.md'

SKIPPABLE_PHRASES = [
    '- Your Highlight at location ',
    '- Your Bookmark at location '
]
NOTE = '- Your Note at location '

def indexOf(obj, elem):
    try:
        ind = obj.index(elem)
        return ind
    except:
        return -1

def elemInLine(listOfElems: list, line: str):
    for elem in listOfElems:
        if indexOf(line, elem) == 0:
            return True
    return False

results = {
    'titles': set()
}

begin = True
quote_next_thought = False
titles = []
end = '=========='
current_title = ''
with open(CLIPPINGS, encoding='utf8') as f:
    for line in f:
        line = line.strip()
        line = line.replace('\ufeff', '')
        if begin:
            results['titles'].add(line)
            current_title = line
            begin = False
        elif line in ['\n', '', ' ']:
            continue
        elif line == end:
            begin = True
            if current_title in results:
                results[current_title].append('\n')
            continue
        elif elemInLine(SKIPPABLE_PHRASES, line):
            continue
        elif indexOf(line, NOTE) == 0:
            quote_next_thought = True
            continue
        else:
            if quote_next_thought:
                line = '> ' + line
                quote_next_thought = False
            if current_title not in results.keys():
                results[current_title] = []
            results[current_title].append(line)


for title in results['titles']:
    title_text = f'# {title}'
    results[title].insert(0, title_text)

def save_highlights(parsed_text, title: str = None):
    if not title:
        title = parsed_text[0][2:]
    title = title.replace('/', '-')
    results_file = open(f'{title}.md', 'w+')
    results_file.write('')
    results_file.close()

    results_file = open(f'{title}.md', 'a')
    lines = ''
    for line in parsed_text:
        lines += line + '\n'
    lines = lines.strip()
    results_file.write(lines)
    results_file.close()

for title in results['titles']:
    save_highlights(results[title])
