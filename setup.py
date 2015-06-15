from setuptools import setup

setup(
    name='wi-prune-branches',
    version='0.0.0',
    py_modules=['prune_branches'],
    install_requires=['GitPython', 'blessings'],
    entry_points={'console_scripts': ['prune_branches=prune_branches:main']}
)
