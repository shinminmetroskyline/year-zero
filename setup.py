

"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['yz_main.py']
DATA_FILES = ["frc_days.py"]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options=dict(py2app=dict(
        plist=dict(
        LSBackgroundOnly=True,
        ),
        )),
    setup_requires=['py2app'],
    plist=dict(
        LSBackgroundOnly=True,
        # LSUIElement=True,
    )
)

