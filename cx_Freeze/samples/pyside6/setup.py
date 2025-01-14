"""
A simple setup script to create an executable using PySide6. This also
demonstrates how to use excludes to get minimal package size.

test_pyside6.py is a very simple type of PySide6 application.

Run the build process by running the command 'python setup.py build'

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the application.
"""

import sys

from cx_Freeze import Executable, setup

base = "Win32GUI" if sys.platform == "win32" else None

options = {
    "build_exe": {
        # exclude packages that are not really needed
        "excludes": [
            "tkinter",
            "unittest",
            "email",
            "http",
            "xml",
            "pydoc",
        ]
    }
}

executables = [Executable("test_pyside6.py", base=base)]

setup(
    name="simple_PySide6",
    version="0.1",
    description="Sample cx_Freeze PySide6 script",
    options=options,
    executables=executables,
)
