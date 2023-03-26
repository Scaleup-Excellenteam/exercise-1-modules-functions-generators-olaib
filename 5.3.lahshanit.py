import re  # לחששנית

CHUNK_SIZE = 1024  # number of bytes to read at a time
FILE_NAME = 'logo.jpg'
PATTERN = b'[a-z]{5,}!'  # pattern to search for ,thw word must be at least 5 letters long and end with '!'


def read_chunks(filename):
    with open(filename, 'rb') as f:
        while True:
            data = f.read(CHUNK_SIZE)
            if not data:
                break
            yield data


def find_secret_messages(filename, pattern):
    """ this function reads a binary file and extract all the secrets messages from it
    :param pattern: pattern to search for
    :param filename: name of the binary file to read from
    :return:
    """
    reg = re.compile(pattern)

    for chunk in read_chunks(filename):
        for line in chunk.split(b'\n'):
            if reg.findall(line):
                for secret_msg in reg.findall(line):
                    yield secret_msg.decode('ascii')


# ================== MAIN ==================
if __name__ == '__main__':
    for message in find_secret_messages(FILE_NAME, PATTERN):
        print(message)
