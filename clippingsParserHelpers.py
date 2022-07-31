import string

# constants
SKIPPABLE_PHRASES = [
    '- Your Highlight at location ',
    '- Your Bookmark at location '
]
NOTE = '- Your Note at location '
BOOKMARK = '- Your Bookmark at location '
START_OF_HIGHLIGHT = '- Your Highlight at location '
END_OF_HIGHLIGHT = '=========='
HIGHLIGHT_HEADER = '## Highlight #'
# end of constants

def indexOf(obj, elem):
    """
    Rewriting the indexOf method for this file.
    Regular `index` method of Python throws an Exception if the element is not found.
    This one does the traditional returning of -1 if that's the case.

    ## Parameters
    - `obj` - the list or string in which the element needs to be found
    - `elem` - the element that needs to be found

    ## Returns
    - index as `number` if the element is found
    - -1 if not found
    """
    try:
        ind = obj.index(elem)
        return ind
    except:
        return -1

def elemInLine(listOfElems: list, line: str):
    """
    Returns `True` if each element in `listOfElems` is present in the start of `line`.
    Returns `False` otherwise.
    """
    for elem in listOfElems:
        if indexOf(line, elem) == 0:
            return True
    return False


def line_cleanup(line: str):
    line = line.strip().replace('\ufeff', '')
    line = line.replace(
        u'\u2019', u'\u0027'  # replace ’ with '
    ).replace(
        '\u201C', '\u0022'  # replace “ with "
    ).replace(
        '\u201D', '\u0022'  # replace ” with "
    )

    # The following logic is borrowed from:
    # https://stackoverflow.com/questions/92438/stripping-non-printable-characters-from-a-string-in-python
    line = ''.join(filter(lambda c: c in string.printable, line))

    return line
