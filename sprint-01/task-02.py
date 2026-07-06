
# Current collection
scripture = [
    '01001001',
    '01001002',
    '01002001',
    '01002002',
    '01002003',
    '02001001',
    '02001002',
    '02001003',
    '66022021'
]

# Filter by book
book = '01'

# filter by chapter
chapter = '001'


# Constraints
# ----------------------------------------------------------------------------
def checkBookId(book_id):
    return 1 <= int(book_id) <= 66


def checkChapterId(chapter_id):
    return 1 <= int(chapter_id)


def checkVerseId(verse_id):
    return 1 <= int(verse_id)
# ----------------------------------------------------------------------------


# Final function
# ----------------------------------------------------------------------------
def filterBible(scripture, book, chapter):

    # Local variable
    compered_scripture = []
    script_length = 8

    # Checking all scripts from current collection
    for script in scripture:
        
        # Length requirement
        if len(script) == script_length:
            book_id, chapter_id, verse_id = script[:2], script[2:5], script[5:]

            # Check constraints
            if checkBookId(book_id) and checkChapterId(chapter_id) and checkVerseId(verse_id):

                # Compare script by book and chapter
                if script.startswith(book+chapter):

                    # Added script to final response
                    compered_scripture.append(script)

            # Continue when some of the id's don't mech constraints
            else:
                continue

        # Continue when script length less than it should be
        else:
            continue
    
    # Return final list
    return compered_scripture
# ----------------------------------------------------------------------------



print(filterBible(scripture, book, chapter))
