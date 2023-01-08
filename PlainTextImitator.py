# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.

import random


def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    #
    # We assume the "latin1" encoding, which accepts more characters
    # than ASCII (and is more common than utf-8).
    #
    # Other common codings welcome: utf-8, utf-16
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #
    f = open(filename, encoding = 'latin1')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...



#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your text with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)
#

#
# Function #1  (createDictionary)
#
def createDictionary(text):
    """Returns a dictionary of every word in "text" and gives them the value of
       the words that directly follow.

       Example:
       {'Returns: ['a']
       'a': ['dictionary']
       'dictionary': ['of']}

       '$' signifies the beginning of a new sentence.
    """
    LoW = text.split()
    d = {}
    pw = '$'   # previous word

    for word in LoW:

        if pw not in d:
            d[pw] = [word]   # start with a list of one element
        else:
            d[pw] += [word]  # add to the list, already present

        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            pw = '$'
        else:
            pw = word   # pw is the "new" previous word

    return d


#
# Function #2   (generateText)
#
def generateText(d, N):
    """Your docstring here...
    """
    print()  # start by printing a newline
    next_word = '$'

    for i in range(N):
        if next_word[-1] == '.' or next_word[-1] == '!' or next_word[-1] == '?':
            next_word = random.choice(d['$'])
            print(next_word, end = ' ')
        else:
            next_word = random.choice(d[next_word])  # Next word
            print(next_word, end = ' ')

    print()                  # Final print, newline