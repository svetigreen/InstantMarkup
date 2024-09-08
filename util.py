import fileinput

"""
A text block generator
"""


def lines(file):
    """
    Reads lines from the file and yields them.

    :param file: The file to read from.
    :return: Yields lines from the file as they are.
    """

    for line in file:
        yield line
    yield '\n'


def blocks(file):
    """
        Generates blocks of text, separated by empty lines.

        :param file: The file to read from.
        :return: Yields blocks of text.
        """
    block = []

    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':
    input_file = 'test_input.txt'
    block_count = 0  # Initialize the block counter

    # Open the file in read mode to read the lines
    with open(input_file, 'r') as input_file:

        for block in blocks(input_file):
            block_count += 1  # Increment the counter for each block
            print(f"Block {block_count}:\n{block}\n")
