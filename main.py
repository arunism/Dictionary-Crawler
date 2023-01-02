import string
from crawler.extract_link import get_links


if __name__ == '__main__':
    alphabets = string.ascii_lowercase

    for alphabet in alphabets:
        get_links(alphabet)
