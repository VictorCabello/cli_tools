import os
import argparse
import re
import shutil


def isNotDuplicated(filename: str) -> bool:
    """When a fil already exitst the
    system add a suffix like "(#)" where # is
    a number.

    This function return False if the filename
    contains a pattern like "(1)" or "(2)" or
    any number between parentesis.

    >>> isNotDuplicated('file.exe')
    True
    >>> isNotDuplicated("otherFile (1) .pdf")
    False
    """
    return not bool(re.search('(\\d+)', filename))


def isPDF(filename: str) -> bool:
    """Return true if the filname ends with '.pdf'

    >>> isPDF('file.exe')
    False
    >>> isPDF("otherFile.pdf")
    True
    >>> isPDF('malfurmedped')
    False
    """
    return filename.endswith('.pdf')


def isFile(filename: str) -> bool:
    """Return true if the string represents a file
    that exits"""
    return os.path.isfile(filename)


def argumentsInit() -> argparse.ArgumentParser:
    description = """
    This program move all pdf file into a folder and delete
    duplicated.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-t", "--test",
                        help="run unit test",
                        action="store_true")
    args = parser.parse_args()
    return args


class MultiFilter:
    def __init__(self, filters=()):
        self.filters = filters

    def __call__(self, toFilter) -> bool:
        if len(self.filters) == 0:
            raise TypeError("No filter provided")
        return all(myFilter(toFilter) for myFilter in self.filters)


def getFiles() -> list[str]:
    filters = (isPDF, isFile, isNotDuplicated)
    multiFilter = MultiFilter(filters)
    files = filter(multiFilter, os.listdir('.'))
    return list(files)


def createDir(dirName: str) -> None:
    if os.path.exists(dirName):
        return

    os.mkdir(dirName)


def main():
    args = argumentsInit()

    if args.test:
        import doctest
        doctest.testmod()
        return

    outputDir = 'pdfs'
    createDir(outputDir)
    files = getFiles()
    for file in files:
        shutil.copy2(file, outputDir)


if __name__ == "__main__":
    main()
