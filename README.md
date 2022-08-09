# kindle-clippings-parser

## But why tho?
The way Kindle puts all highlighted texts and notes in its "My Clippings.txt" file, in my opinion, is an abomination. It's a text file that's hardly readable, with no structure whatsoever applied to the highlights in relation to the titles, notes and bookmarks. The titles overlap with each other, there is no certainty when a highlight ends and another begins, notes are displyed exactly how regular highlight is displayed and can easily be skipped, and it just looks plain ugly. Simply put, "My Clipping.txt" file is chaos.

This software is a feeble attempt to remedy that. It's a Python file that can run through the clippings file and:
- create a markdown file for each title, with the same name as the title name;
- put all the highlights for each title over there;
- separate each highlight with a header; and
- your notes will be styled as quotes.

## An Example
In the below example:
- top left: how the Clippings.txt file looks
- bottom left: how the parsed markdown file looks for one of the books in the clippings file
- right: how the said markdown file looks with a markdown reader

![](./assets/clippings-md-preview.png)


## Prerequisites
All you need is **Python 3**, particularly a more recent build of Python that supports f-strings and type hints.

## Execution
Running this project simply means executing the "clippings-parser-2.py" Python file. (There is an OG "clippings-parser.py", but that's more of a low-effort proof-of-concept than an actual working piece of software.)

```sh
python clippings-parser-2.py

# or:
python3 clippings-parser-2.py
```

## Is it perfect?
No, certainly not. A large part of its issues will lie with how haphazardly Kindle organizes its highlights. For example, some notes texts are placed before the highlight from the book, and some after the highlight. So far, it hasn't been possible for me to point out whether the note belongs to the highlight above or the highlight below, so that issue is not solved by this software. Here, it will put the note before or after the text that proceeds it, depending on how it is presented in the clippings file, and therefore might give into some inaccuracies.

There might be a few other shortcomings, and a super-simple app like this means there is always room for improvement, and I will try to add more features to it if I get enough time. But for now, this will have to do.

## That's it
You may add more features to it by creating a PR. Hope this helps!
