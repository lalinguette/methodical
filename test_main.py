from main import extract_all_headlines, open_file, detect_max_depth, add_depth, reset_counter, assemble_toc

data = """# Headline 1

blabla

## Headline 1.1

## Headline 1.2

### Headline 1.2.1

## Headline 1.3
"""

data_cleaned = ['# Headline 1', '', 'blabla', '', '## Headline 1.1', '', '## Headline 1.2', '', '### Headline 1.2.1', '', '## Headline 1.3']
headlines = ['# Headline 1', '## Headline 1.1', '## Headline 1.2', '### Headline 1.2.1', '## Headline 1.3']


def test_open():
    actual = open_file()
    data_ = data.splitlines()
    assert actual == data_


def test_extract():
    len_headlines = 5
    actual = len(extract_all_headlines(data_cleaned))

    assert actual == len_headlines

def test_detect_max():
    actual = detect_max_depth(data_cleaned)
    assert actual == 3

def test_add_depth():
    actual = add_depth(headlines, 3)
    expected = ["1.0.0 Headline 1",
    "1.1.0 Headline 1.1",
    "1.2.0 Headline 1.2",
    "1.2.1 Headline 1.2.1",
    "1.3.0 Headline 1.3", ]
    assert actual == expected


def test_resset_counter():
    counter = [1, 2, 3]
    new_counter = [1, 2, 0]

    actual = reset_counter(counter, old_pos=2)

    assert actual == new_counter

def test_assemble_toc():
    expected = """# Table of Contents
1.0.0 Headline 1
1.1.0 Headline 1.1
1.2.0 Headline 1.2
1.2.1 Headline 1.2.1
1.3.0 Headline 1.3"""
    input_ = ["1.0.0 Headline 1",
"1.1.0 Headline 1.1",
"1.2.0 Headline 1.2",
"1.2.1 Headline 1.2.1",
"1.3.0 Headline 1.3", ]
    actual = assemble_toc(input_)
    assert actual == expected