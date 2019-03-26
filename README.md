# DayOneImport

A script to import old journal entries from Penzu to Day One.

## Preqrequisites

- [Python 3](https://www.python.org/downloads/) in installed on OS X.
- [Day One](https://dayoneapp.com/) v2 is installed on OS X.
- The [Day One CLI v2](https://help.dayoneapp.com/tips-and-tutorials/command-line-interface-cli) is installed on OS X. [Install](https://help.dayoneapp.com/tips-and-tutorials/command-line-interface-cli) the Day One CLI v2 by running `sudo bash /Applications/Day\ One.app/Contents/Resources/install_cli.sh`.

## Running The Script

1. Create a new journal for the imported entries. Also recommended for testing.
1. Create a journal.txt file in this directory containing the journal entries to be imported. See format details below.
1. Update the `entryJournal`, `entryTimeZone`, and `entryTags` variables in the `import.py` script if needed.
1. Run `python3 import.py` to import the entries.
1. Verify the import was successful by checking the summary printed at the end of the script `Summary: 0 errors for 101 entries`.

## Format of Import File (journal.txt)

Note: Line spacing and multiple lines don't matter.

```
Entry Title
---
Entry body.  Stuff stuff stuff.  Stuff stuff stuff.

Stuff stuff stuff.  Stuff stuff stuff. Stuff stuff stuff.

2011-05-18 8:29pm UTC


Entry Title
---
Entry body.  Stuff stuff stuff.  Stuff stuff stuff.

Stuff stuff stuff.  Stuff stuff stuff. Stuff stuff stuff.

2011-05-18 8:29pm UTC


Entry Title
---
Entry body.  Stuff stuff stuff.  Stuff stuff stuff.

Stuff stuff stuff.  Stuff stuff stuff. Stuff stuff stuff.

2011-05-18 8:29pm UTC
```

Adjust the import script as needed to match different import formats.
