import re
import subprocess
from pathlib import Path

# import the journal export
path = Path("journal.txt")
file = path.read_text()

# get each entry
# escape characters in body
matcher = re.compile('(.*)\n---\n([^\d\d\d\d]*)(\d.*UTC)')
matches = matcher.finditer(file)

i = 0
e = 0
for match in matches:
    i += 1
    entryTitle = match[1]
    entryBody = match[2]
    entry = f"{entryTitle}\n\n{entryBody}"
    entryDate = match[3]
    entryTags = "Penzu"
    entryJournal = "Import"
    entryTimeZone = "America/Denver"
    print(i)
    print("-------------",
          "\nTitle: ",
          entryTitle,
          "\nDate: ",
          entryDate,
          "\nBody: ",
          '\n' + entryBody,
          "\n-------------")

    result = subprocess.call(['dayone2', 'new',
                              entry,
                              '--journal', entryJournal,
                              '--time-zone', entryTimeZone,
                              '--date', entryDate,
                              '--tags', entryTags])

    if result != 0:
        e += 1

print(f"\n\n\n\nSummary: {e} errors for {i} entries")
