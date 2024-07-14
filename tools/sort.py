import os
import argparse
import re
import shutil
from typing import TypedDict
from pathlib import Path


def main():
    args = get_cli_args()
    if args['unittest']:
        runDocTests()
        return
    movePDF(args['target'], args['source'])


class CLIArgsType(TypedDict):
    unittest: bool
    target: str
    source: str


def dir_path(path: str) -> str:
    if os.path.exists(path):
        return path
    else:
        raise NotADirectoryError(path)


def get_cli_args() -> CLIArgsType:
    description = """
    This program move all pdf file into a folder and delete
    duplicated.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-ut", "--unittest",
                        help="run unit test",
                        action="store_true")
    parser.add_argument("--target",
                        type=dir_path,
                        help="path to target directory",
                        default='./pdfs',
                        action="store")
    parser.add_argument("source",
                        type=dir_path,
                        help="path to source directory",
                        nargs='?',
                        default='.',
                        action="store")
    args = parser.parse_args()
    return vars(args)


def runDocTests() -> None:
    """
    Runs the doctests defined in the module.

    This function uses `doctest.testmod()` to automatically find and run all
    the doctests in the module. Doctests are snippets of interactive Python
    sessions that are embedded in the docstrings of functions, classes, and
    modules.

    Doctests are a convenient way to both test your code and provide examples
    of how it works.

    """
    import doctest
    doctest.testmod()


def movePDF(trgDirPath: str, srcDirPath: str) -> None:
    createDir(trgDirPath)
    print(srcDirPath)
    files = getFiles(srcDirPath)
    print(files)
    for file in files:
        shutil.copy2(file, trgDirPath)


def isNotDuplicated(filename: Path) -> bool:
    return not bool(re.search('(\\d+)', filename.stem))


def isPDF(filename: Path) -> bool:
    return filename.suffix == '.pdf'


def isFile(filename: Path) -> bool:
    return os.path.isfile(filename)


class MultiFilter:
    def __init__(self, filters=()):
        self.filters = filters

    def __call__(self, toFilter) -> bool:
        if len(self.filters) == 0:
            raise TypeError("No filter provided")
        return all(myFilter(toFilter) for myFilter in self.filters)


def getFiles(srcDirPath: str) -> list[str]:
    filters = (isPDF, isFile, isNotDuplicated)
    multiFilter = MultiFilter(filters)
    p = Path(srcDirPath)
    files = filter(multiFilter, list(p.iterdir()))
    return list(files)


def createDir(dirName: str) -> None:
    if os.path.exists(dirName):
        return

    os.mkdir(dirName)


if __name__ == "__main__":
    main()
