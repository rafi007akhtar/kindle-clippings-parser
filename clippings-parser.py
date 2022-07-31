import string
from clippingsParserHelpers import *

# Location of the clippings file
CLIPPINGS = 'My Clippings.txt'

# constants
SKIPPABLE_PHRASES = [
    '- Your Highlight at location ',
    '- Your Bookmark at location '
]
NOTE = '- Your Note at location '
END_OF_HIGHLIGHT = '=========='
HIGHLIGHT_HEADER = '## Highlight #'

# this method will create a new title
def create_new_title():
    return {
        'highlights': [],
        'meta-data': {
            'highlight-header-number': 0
        }
    }

# this result will contain all the parsed results
results = {
    'titles': set()
    # title: {} <- this dict will contain all highlights, and will be accessible through the book title as key
}

# main logic for putting in the highlights in an array based on the titles
new_highlight = True
quote_next_thought = False
current_title = ''
skip_next_header = False
with open(CLIPPINGS, encoding='utf') as f:
    for line in f:
        # # clean up each line
        # line = line.strip()
        # line = line.replace('\ufeff', '')
        line = line_cleanup(line)

        # parse the line based on what it contains
        if new_highlight:
            results['titles'].add(line)
            current_title = line
            new_highlight = False
        elif (
            line in ['\n', '', ' '] or
            elemInLine(SKIPPABLE_PHRASES, line)
        ):
            continue
        elif line == END_OF_HIGHLIGHT:
            new_highlight = True  # next one will be a new highlight since we reached the end for the current one
            if current_title in results:
                results[current_title]['highlights'].append('\n')
            continue
        elif indexOf(line, NOTE) == 0:
            quote_next_thought = True  # clippings file announcing the next line is my note, so it should apply the quotes markdown style
            continue
        else:
            if quote_next_thought:
                line = '> ' + line
            if current_title not in results.keys():
                results[current_title] = create_new_title()

            if not skip_next_header:
                n = results[current_title]['meta-data']['highlight-header-number'] + 1
                results[current_title]['highlights'].append(f'{HIGHLIGHT_HEADER}{n} \n')
                results[current_title]['meta-data']['highlight-header-number'] += 1
            else:
                skip_next_header = False

            results[current_title]['highlights'].append(line)

            if quote_next_thought:
                quote_next_thought = False
                skip_next_header = True


# prepend the title of the book as a heading to its highlights
for title in results['titles']:
    title_text = f'# {title}'
    results[title]['highlights'].insert(0, title_text)

# method used for creating a new MD file for a title and
# dumping all highlights there
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

# for each title, save the highlights in a new file
for title in results['titles']:
    save_highlights(results[title]['highlights'])

def __main__():
    pass
