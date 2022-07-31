from typing import List
from clippingsParserHelpers import *

# Location of clippings file
# TODO: import this with a YAML file later
CLIPPINGS = 'My Clippings.txt'

highlights = {
    'titles': [],
}

highlight_begins = True
highlight_type = 'highlight'  # it can be 'highlight' or 'note'
current_book = ''
end_of_highlight = False  # will be used for new notes

# def __main__():
# print('getting inside main')
with open(CLIPPINGS, encoding='utf') as f:
    # global highlight_type, current_book, highlight_begins

    for line in f:
        # At first, perform the file cleanup
        line = line_cleanup(line)

        if highlight_begins:
            highlight_begins = False
            current_title = line
            if line not in highlights['titles']:
                highlights['titles'].append(line)
                highlights[current_title] = []
        elif line in ['\n', '', ' ']:
            continue
        elif indexOf(line, START_OF_HIGHLIGHT) == 0:
            highlight_type = 'highlight'
        elif indexOf(line, NOTE) == 0:
            highlight_type = 'note'
        elif indexOf(line, END_OF_HIGHLIGHT) == 0:
            highlight_begins = True
            end_of_highlight = True
        elif indexOf(line, BOOKMARK) == 0:
            continue
        else:
            highlights[current_title].append((line, highlight_type, end_of_highlight))
            if end_of_highlight:
                end_of_highlight = False

print(highlights)

def save_highlights(title: str, book_highlights: List):
    title = title.replace('/', '-')
    md_file = open(f'{title}.md', 'w+')
    md_file.write('')
    md_file.close()

    highlight_ind = 1

    md_file = open(f'{title}.md', 'a')
    for highlight in book_highlights:
        htext, htype, hend = highlight
        htext = htext.strip() + '\n'
        if htype == 'highlight':
            md_file.write(f'{HIGHLIGHT_HEADER}{highlight_ind}\n')
            md_file.write(htext)
            highlight_ind += 1
        elif htype == 'note':
            if hend:
                md_file.write('\n')  # It's a new note
            md_file.write(f'> {htext}')
    md_file.close()

for title in highlights['titles']:
    save_highlights(title, highlights[title])
