"""
This script moves all PDF files from a source directory to a target directory
and deletes duplicates.

Usage:
    python script_name.py [--unittest] [--target TARGET_DIR] [SOURCE_DIR]

Options:
    -ut, --unittest    Run unit tests using doctest.
    --target           Path to the target directory (default: ./pdfs).
    SOURCE_DIR         Path to the source directory (default: current directory).

Functions:
    main(): Main entry point of the script.
    get_cli_args() -> CLIArgsType: Configures and parses the command-line
    arguments.
    runDocTests() -> None: Runs the doctests defined in the module.
    movePDF(trgDirPath: str, srcDirPath: str) -> None: Moves PDF files to a
    specified folder and removes duplicates.
    isNotDuplicated(filename: Path) -> bool: Checks if a file is not a
    duplicate.
    isPDF(filename: Path) -> bool: Checks if a file has a .pdf extension.
    isFile(filename: Path) -> bool: Checks if a string represents an existing
    file.
    getFiles(srcDirPath: str) -> list[str]: Retrieves a list of valid PDF
    files in the specified directory.
    createDir(dirName: str) -> None: Creates a directory if it doesn't exist.
    dir_path(path: str) -> str: Validates if the provided path is an existing
    directory.

Classes:
    CLIArgsType(TypedDict): Type definition for command-line arguments.
    MultiFilter: Class to apply multiple filter functions to a list of files.
"""

import os
import argparse
import re
import shutil
from typing import TypedDict
from pathlib import Path


def main():
    """
    Main entry point of the script.

    Parses command-line arguments and either runs tests or moves PDF files
    based on the provided arguments.
    """
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
    """
    Validates if the provided path is an existing directory.

    Args:
        path (str): The directory path to validate.

    Returns:
        str: The validated directory path.

    Raises:
        NotADirectoryError: If the provided path does not exist.

    Example:
        >>> dir_path(".")
        '.'
        >>> dir_path("non_existing_dir")  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        NotADirectoryError: non_existing_dir
    """
    if os.path.exists(path):
        return path
    else:
        raise NotADirectoryError(path)


def get_cli_args() -> CLIArgsType:
    """
    Configures and parses the command-line arguments.

    Returns:
        CLIArgsType: A dictionary containing the following keys:
            - unittest (bool): Flag to run unit tests.
            - target (str): Path to the target directory.
            - source (str): Path to the source directory.

    Example:
        >>> args = get_cli_args()
        >>> isinstance(args, dict)
        True
        >>> 'unittest' in args
        True
        >>> 'target' in args
        True
        >>> 'source' in args
        True
    """
    description = """
    This program moves all PDF files into a folder and deletes duplicates.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-ut", "--unittest",
                        help="run unit test",
                        action="store_true")
    parser.add_argument("--target",
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
    """
    Moves PDF files to a specified folder and removes duplicates.

    This function collects all PDF files in the specified source directory,
    copies them to the target directory, and ensures no duplicate files are
    moved.

    Args:
        trgDirPath (str): The target directory path.
        srcDirPath (str): The source directory path.
    """
    createDir(trgDirPath)
    files = getFiles(srcDirPath)
    for file in files:
        shutil.copy2(file, trgDirPath)


def isNotDuplicated(filename: Path) -> bool:
    """
    Checks if a file is not a duplicate.

    When a file already exists, the system adds a suffix like "(#)" where #
    is a number. This function returns False if the filename contains a
    pattern like "(1)" or "(2)" or any number in parentheses.

    Args:
        filename (Path): The name of the file to check.

    Returns:
        bool: True if the file is not a duplicate, False otherwise.

    Examples:
        >>> isNotDuplicated(Path('file.pdf'))
        True
        >>> isNotDuplicated(Path("otherFile (1).pdf"))
        False
    """
    return not bool(re.search(r'\(\d+\)', filename.stem))


def isPDF(filename: Path) -> bool:
    """
    Checks if a file has a .pdf extension.

    Args:
        filename (Path): The name of the file to check.

    Returns:
        bool: True if the file has a .pdf extension, False otherwise.

    Examples:
        >>> isPDF(Path('file.pdf'))
        True
        >>> isPDF(Path('file.txt'))
        False
    """
    return filename.suffix == '.pdf'


def isFile(filename: Path) -> bool:
    """
    Checks if a string represents an existing file.

    Args:
        filename (Path): The name of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.

    Examples:
        >>> isFile(Path(__file__))
        True
        >>> isFile(Path('non_existing_file.txt'))
        False
    """
    return os.path.isfile(filename)


class MultiFilter:
    """
    A class to apply multiple filter functions to a list of files.

    Attributes:
        filters (tuple): A tuple of filter functions to apply.
    """

    def __init__(self, filters=()):
        """
        Initializes MultiFilter with a tuple of filter functions.

        Args:
            filters (tuple): A tuple of filter functions to apply.
        """
        self.filters = filters

    def __call__(self, toFilter) -> bool:
        """
        Applies all filter functions to the given item.

        Args:
            toFilter: The item to apply the filters to.

        Returns:
            bool: True if the item passes all filters, False otherwise.

        Raises:
            TypeError: If no filters are provided.
        """
        if len(self.filters) == 0:
            raise TypeError("No filter provided")
        return all(myFilter(toFilter) for myFilter in self.filters)


def getFiles(srcDirPath: str) -> list[str]:
    """
    Retrieves a list of valid PDF files in the specified directory.

    This function filters the files in the specified directory using a set
    of filter functions to ensure they are PDF files, they exist, and
    they are not duplicates.

    Args:
        srcDirPath (str): The source directory path.

    Returns:
        list[str]: A list of valid PDF files.

    Example:
        >>> p = Path('.')
        >>> p.mkdir(exist_ok=True)
        >>> f = p / 'testfile.pdf'
        >>> f.touch()
        >>> getFiles('.') == [f]
        True
        >>> f.unlink()
    """
    filters = (isPDF, isFile, isNotDuplicated)
    multiFilter = MultiFilter(filters)
    p = Path(srcDirPath)
    files = filter(multiFilter, list(p.iterdir()))
    return list(files)


def createDir(dirName: str) -> None:
    """
    Creates a directory if it doesn't exist.

    Args:
        dirName (str): The name of the directory to create.

    Example:
        >>> p = Path('test_dir')
        >>> p.exists()
        False
        >>> createDir(str(p))
        >>> p.exists()
        True
        >>> p.rmdir()
    """
    if os.path.exists(dirName):
        return

    os.mkdir(dirName)


if __name__ == "__main__":
    main()
