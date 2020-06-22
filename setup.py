import sys
from cx_Freeze import setup, Executable

base = None


excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml', 'bz2']
if (sys.platform == "win32"):
    base = "Win32GUI"

exe = Executable(
        script="main.py",
        icon="calculator-interface.ico",
        targetName="simple-stack-calculator",
        base=base
        )
includefiles = ["calculator-interface.ico"]

setup(
    name = "Simple stack Calculator",
    version="0.1",
    description="Calculates :)",
    author="vint",
    options={'build_exe': {'include_files': includefiles, 'excludes': excludes, 'optimize': 2}},
    executables=[exe]
)