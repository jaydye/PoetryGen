# PoetryGen
## a tool for generating poetry

Requirements:

-python3

-[markovify](https://github.com/jsvine/markovify)

-[pysle](https://pypi.org/project/pysle/#installation) and the

-[ISLEdict.txt

-file](https://raw.githubusercontent.com/uiuc-sst/g2ps/master/English/ISLEdict.txt)

About:

Generates markov chain-based sentences based on input text files.
Generated sentences are then checked by the pysle pronunciationtools to
determine whether they are iambic, i.e. alternating unstressed and
stressed syllables, and whether they are 10 syllables long, i.e.
pentameter.

It turns out that the current algorithm for brute forcing these iambic
pentameter lines takes a very long time to find any, so the script is
currently set to output all 10-syllable to lines to one text file, with
another text file being reserved for the imabic pentameter lines.
