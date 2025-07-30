"""
Small program that takes a markdown file as input.
The headlines are extracted and put and parsed into a table of contents with chapter numbers
"""
# todo: run tests automatically
# todo: run linter automatically

def open_file() -> list:
    """
    open and read file. Return content as list split on line breaks
    :return: list
    """
    # todo: take given file
    with open("../methodical/example.md", "r",) as f:
        file = f.read()
        file = file.splitlines()
    return file

def extract_all_headlines(file: list) -> list:
    """
    filter lines in file and return only those that are marked as a headline
    :param file: list of strings
    :return: smaller list of strings, all starting with "#"
    """
    headlines = [line for line in file if line.startswith("#")]
    return headlines

def detect_max_depth(headlines: list) -> int:
    """
    detect the maximum depth the chapter numbers of the TOC will need
    :param headlines: list of strings starting with "#"
    :return: int
    """
    depth = max([hl.count("#") for hl in headlines])
    return depth

def reset_counter(counter, old_pos):
    for i, c in enumerate(counter):
        if i >= old_pos:
            counter[i] = 0

    return counter

def add_depth(headlines: list, max_depth: int) -> list:
    """
    add chapter numbers of correct depth to each headline. remove the markdown marker
    :param headlines: list of strings starting with "#"
    :param max_depth: integer of the depth the ToC should take
    :return: list of new strings
    """
    # todo: remove trailing zeros
    result = []
    counter = [0]*max_depth
    old_pos = 0
    for hl in headlines:
        pos = hl.count("#") - 1
        if pos < old_pos:
            counter = reset_counter(counter, old_pos)
        counter[pos] = counter[pos] + 1
        new_headline = ".".join(str(el) for el in counter) + " " + hl.strip("#").strip()
        result.append(new_headline)
        old_pos = pos
    return result


def main():
    file = open_file()
    headlines = extract_all_headlines(file)
    max_depth = detect_max_depth(headlines)
    # todo: add links to chapters


if __name__ == '__main__':
    # todo: arg parser to give files
    main()