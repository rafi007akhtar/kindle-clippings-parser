from typing import List
from clippingsParserHelpers import *

# Location of clippings file
# TODO: import this with a YAML file later
CLIPPINGS = 'My Clippings.txt'

highlights = {
    'titles': [],
    # It will also have the following list-of-tuples for each book:
    # book-title: [(
    #   highlighted-text <str>,
    #   highlight-type <'highlight' | 'note'>,
    #   brand-new-highlight <bool>
    # )]
}

highlight_begins = True
highlight_type = 'highlight'  # TODO: reinforce type so it can only be 'highlight' or 'note'
current_title = ''
brand_new_highlight = False  # will be used for new notes

with open(CLIPPINGS, encoding='utf') as f:

    for line in f:
        # At first, perform the line cleanup
        line = line_cleanup(line)

        # next, depending on the type of line, parse it
        if highlight_begins:
            current_title = line
            if line not in highlights['titles']:  # `titles` is an array of string containing all the book titles
                highlights['titles'].append(line)
                highlights[current_title] = []
            highlight_begins = False

        elif line in ['\n', '', ' ']:
            continue

        # distinguish between a highlight and a note
        elif indexOf(line, START_OF_HIGHLIGHT) == 0:
            highlight_type = 'highlight'
        elif indexOf(line, NOTE) == 0:
            highlight_type = 'note'

        elif indexOf(line, END_OF_HIGHLIGHT) == 0:
            highlight_begins = True
            brand_new_highlight = True  # the next highlight will be a brand new highlight
        elif indexOf(line, BOOKMARK) == 0:
            continue  # simply skip the bookmarks

        else:
            # save the highlighted text in (text, type, bool) format, where bool is for a brand new highlight
            highlights[current_title].append((line, highlight_type, brand_new_highlight))
            if brand_new_highlight:
                brand_new_highlight = False

print(highlights)

def save_highlights(title: str, book_highlights: List):
    """
    Takes the highlights of one book, and saves those in a user-readable markdown file.

    ### Styles used
        - Each highlight begings with an h2 header followed by the term 'Highlight' followed by the highlights number
        - Each note (presumably would) follow its corresponding highlight
        - Each note is presented as a quote
    
    ### Parameters
    - `title`: title of the book from the `highlights` dictionary
    - `book_highlights`: list-of-tuples containing the parsed text of the highlights (basically `highlights['book-name']`)
    """
    title = title.replace('/', '-')
    md_file = open(f'{title}.md', 'w+')
    md_file.write('')
    md_file.close()

    highlight_ind = 1

    md_file = open(f'{title}.md', 'a')
    for highlight in book_highlights:
        hText, hType, hEnd = highlight
        hText = hText.strip() + '\n'
        if hType == 'highlight':
            md_file.write(f'{HIGHLIGHT_HEADER}{highlight_ind}\n')
            md_file.write(hText)
            highlight_ind += 1
        elif hType == 'note':
            if hEnd:
                md_file.write('\n')  # It's a new note
            md_file.write(f'> {hText}')
    md_file.close()

for title in highlights['titles']:
    save_highlights(title, highlights[title])
